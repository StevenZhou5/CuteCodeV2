# coding=utf-8
"""
Encoder model
"""
__author__ = 'Steven Zhou'

import numpy as np
import torch
from torch import nn

import dataset


# =========================================================<editor-fold des="公共方法相关">=========================================================
def get_sinusoid_embedding_position_matrix(max_seq_len, embedding_dim, padding_idx=None):
    """
    Sinusoid position encoding table : 正弦型号未知编码矩阵
    :param max_seq_len: 最大句子长度(注意是全局最大句子长度，不是batch中最大句子长度)
    :param embedding_dim: 位置编码输出的维度数，这个要和word的embedding_dim的维数相同
    :param padding_idx: 如果有PAD的占位，那么这个PAD占位的one-hot编码是多少，如果给定，那么最后关于PAD的embedding编码将全为0
    :return: 一个size 为[max_seq_len,embedding_size]的embedding矩阵
    """

    def cal_angle(position_i, embedding_j):
        """
        embedding矩阵初始(i,j)元的值
        :param position_i: 矩阵的第i行：对应是是位置i
        :param embedding_j: 矩阵的第j列：对应的是位置i在第j个embedding维度上的坐标值
        :return: i/((10000^(2*(j//2))*embedding_size) ： 对于给定位置i不变，j越大值越小；对于给定j不变，i越大值越大
        """
        return position_i / np.power(10000, 2 * (embedding_j // 2) / embedding_dim)

    def get_position_i_angle_vec(position_i):
        """
        获取第i行所有元素的值：即one-hot位置编码为i的初始embedding编码
        :param position_i: 第i行
        :return: 位置i的初始embedding编码
        """
        return [cal_angle(position_i, embedding_j) for embedding_j in range(embedding_dim)]

    # 首先生成一个size 为[max_seq_len,embedding_size]的embedding矩阵，并初始化每一个(i,j)元
    sinusoid_matrix = np.array([get_position_i_angle_vec(pos_i) for pos_i in range(max_seq_len)])

    #
    sinusoid_matrix[:, 0::2] = np.sin(sinusoid_matrix[:, 0::2])  # dim 2i
    sinusoid_matrix[:, 1::2] = np.cos(sinusoid_matrix[:, 1::2])  # dim 2i+1

    # 将占位PAD的embedding值全部置为0
    if padding_idx is not None:
        # zero vector for padding dimension
        sinusoid_matrix[padding_idx] = 0.

    assert sinusoid_matrix.shape == (max_seq_len, embedding_dim)
    return torch.FloatTensor(sinusoid_matrix)


def get_non_pad_mask(seq):
    """
    将pad位置置为0，其他位置置为1的mask矩阵
    :param seq: [batch_size,batch_seq_len]
    :return: [batch_size,batch_seq_len,1]
    """
    assert seq.dim() == 2
    # ne(dataset.PAD)就是把不等于dataset.PAD的值置为TRUE，等于dataset.PAD置为FALSE
    # type(torch.float) 就是把true/false转为1./0.的float类型值
    # unsqueeze(-1)就是把size [batch_size,batch_seq_len] 扩展一维变成 [batch_size,batch_seq_len,1]
    return seq.ne(dataset.PAD).type(torch.float).unsqueeze(-1)


def get_self_attention_q_k_pad_mask(seq_q, seq_k):
    """
    在q,k进行举证相乘然后在softmax进行求attention权重时需要将PAD位置的注意力权重置为零
    注意:batch_seq_q_len和batch_seq_k_v_len不一定一样，因为在decoder的第二层MultiHeadAttentionLayer时q是target语言，k是encoder的输出
    :param seq_q: [batch_size,batch_seq_q_len]
    :param seq_k: [batch_size,batch_seq_k_v_len]
    :return: [batch_size,batch_seq_q_len,batch_seq_k_v_len]
    """
    len_seq_q = seq_q.size(1)  # 取出q的句子长度：这里必须是取出q的len

    # 这里mask时需要将等于dataset.PAD的位置的值置为1，到后面会被变成负无穷
    attention_q_k_pad_mask = seq_k.eq(dataset.PAD)  # [batch_size,batch_seq_k_v_len]
    # 在维度1上增加一个维度
    attention_q_k_pad_mask = attention_q_k_pad_mask.unsqueeze(1)  # [batch_size,1,batch_seq_k_v_len]
    # 把拉升出来的维度1进行扩展len_seq_q倍
    attention_q_k_pad_mask = attention_q_k_pad_mask.expand(-1, len_seq_q,
                                                           -1)  # [batch_size,batch_seq_q_len,batch_seq_k_v_len]
    return attention_q_k_pad_mask


def get_do_not_see_subsequent_mask(seq):
    """
    不能去看后面的词：用上三角矩阵去把后面的词盖住
    :param seq: 需要mask的句子的原始信息:[batch_size,seq_len]
    :return: [batch_size,[seq_len],[seq_len]]
    """
    # 先得到batch_size,seq_len
    batch_size, seq_len = seq.size()

    # 构建一个[seq_len,seq_len]的全为1的矩阵
    result_mask = torch.ones(seq_len, seq_len, device=seq.device, dtype=torch.uint8)  # [seq_len,seq_len]
    # 将[seq_len,seq_len]的result_mask变为上三角形行列式，主对角线元素也要为0：为0的地方代表可以看到的地方，预测下一个的时候，当前这个是可以看的
    result_mask = torch.triu(result_mask, diagonal=1)  # diagonal=1则主对角线元素也为0: [seq_len,seq_len]

    # 最后将构造好的矩阵进行扩展为:[batch_size,seq_len,seq_len]
    result_mask = result_mask.unsqueeze(0).expand(batch_size, -1, -1)

    return result_mask


# </editor-fold>


# =========================================================<editor-fold des="公共模型相关">=========================================================
class SelfAttentionLayer(nn.Module):
    """
    SelfAttention layer:
    """

    def __init__(self, temperature, self_attention_dropout=0.1):
        """
        :param temperature: "温度"：用于调整句子中某个词对句子中其他词的关注度占比：T越大那些原先占比小的就会有越大的关注度占比
        :param self_attention_dropout:
        """
        super(SelfAttentionLayer, self).__init__()

        # 在计算完q,k矩阵的点积之后要除以一个temperature，然后在进行softmax，不然一开始Attention值较小的在softmax之后权重会趋于0，这不利于模型的学习
        # 这个值跟知识蒸馏中的temperature含义一样(T必须大于1，T越小只能提取出权重占比越大的特征，而占比小的特征将"蒸"不出来，T过大又会把无关痛痒的特征也"蒸"出来，干扰模型的预测)
        # tensor([0.8000, 0.1000, 0.0800, 0.0200]) :
        # 温度为1时: tensor([0.4095, 0.2034, 0.1993, 0.1877])
        # 温度为2时: tensor([0.3247, 0.2288, 0.2266, 0.2199])
        # 温度为0.5时： tensor([0.5904, 0.1456, 0.1399, 0.1241])
        self.temperature = temperature

        self.dropout = nn.Dropout(self_attention_dropout)

        # input_size:[num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]  output_size:[num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]
        self.softmax = nn.Softmax(dim=2)

    def forward(self, q, k, v, mask=None):
        """
        注意q和kv的len不一定一样：q和k的q_k_out_dim必须一样，k和v的batch_seq_k_v_len必须一样
        :param q: [num_head * batch_size,batch_seq_q_len,q_k_out_dim]
        :param k: [num_head * batch_size,batch_seq_k_v_len,q_k_out_dim]
        :param v: [num_head * batch_size,batch_seq_k_v_len,v_out_dim]
        :param mask: [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]
        :return:
        """
        # input: q:[num_head * batch_size,batch_seq_q_len,q_k_out_dim];  k:[num_head * batch_size,batch_seq_k_v_len, q_k_out_dim]
        # output: [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]
        attention = torch.bmm(q, k.transpose(1, 2))

        attention = attention / self.temperature  # [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]

        if mask is not None:
            # mask 如果是一个size和attention完全一样的上三角矩阵：主对角线以下全为零，其余位置全为1；这样的目的是为了让句子中每个词只注意一下它前面的词
            # masked_fill会把mask中为1的位置对应于attention矩阵中值都置为 - np.inf
            # 为什么是 负无穷而不是0是因为后面在进行softmax的时候要执行exe操作(e^x次幂):当x=负无穷时，
            attention = attention.masked_fill(mask, -np.inf)  # -np.inf代表负无穷

        # 进行softmax:得到每个词应该对其他句子中所有值产生的注意力权重（0-1）
        attention = self.softmax(attention)  # [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]
        # dropout操作
        attention = self.dropout(attention)  # [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]

        # 最终输出加了selfAttention的v矩阵
        # input:attention: [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]; v :[num_head * batch_size,batch_seq_q_len, v_out_dim]
        output = torch.bmm(attention, v)  # [num_head * batch_size, batch_seq_q_len,  v_out_dim]

        return output, attention


class MultiHeadAttentionLayer(nn.Module):
    """
    使用num_head个q，k,v计算出num_head个value值，然后在将他们连接起来，然后在进行全连接
    注意：(1)embedding_dim要和word embedding输出的维度一致; (2) q,k的输出维度要一致；(3)q,k,v的输入维度都要是embedding_dim
    """

    def __init__(self, num_head, embedding_dim, q_k_out_dim, v_out_dim, multi_attention_dropout=0.1,
                 self_attention_dropout=0.1):
        """
        :param num_head: 需要多少的head，一个head对应的就是某一种关注关系(比如:主谓之间的关系；代词的指代关系)
        :param embedding_dim: one-hot的词与位置编码被embedding后的维度,在进行全连接变换后的维度，如果不做变换就等于embedding_dim
        :param q_k_out_dim: q，k的输出维度必须一致
        :param v_out_dim: v 的输出维度
        :param multi_attention_dropout:
        """
        super(MultiHeadAttentionLayer, self).__init__()

        self.num_head = num_head
        self.q_k_out_dim = q_k_out_dim
        self.v_out_dim = v_out_dim

        # 通过word embedding + pos embedding之后的句子信息作为输入，进行q,k,v的计算
        # 针对q，k的输入与输出维度一致：input size:[batch_size,batch_seq_len,embedding_dim]; output size:[batch_size,batch_seq_len,num_head * q_k_out_dim]
        self.w_q = nn.Linear(embedding_dim, num_head * q_k_out_dim)
        self.w_k = nn.Linear(embedding_dim, num_head * q_k_out_dim)
        # 使用正太分布进行权重的初始化: 大部分的值会分布在[mean -std,mean+std]之间
        q_k_std = np.sqrt(2.0 / (embedding_dim + q_k_out_dim))
        nn.init.normal_(self.w_q.weight, mean=0.0, std=q_k_std)  # mean是正太分布的均值，std是正太分布的标准差
        nn.init.normal_(self.w_k.weight, mean=0.0, std=q_k_std)

        # 针对v的input size与k一致(不需要与q一致，因为在decoder的时候q是target语言，其句子长度是不等于source语言的长度的)，output size:[batch_size,seq_len,num_head * v_out_dim]
        self.w_v = nn.Linear(embedding_dim, num_head * v_out_dim)
        v_std = np.sqrt(2.0 / (embedding_dim + v_out_dim))
        self.w_v.weight.data.normal_(mean=0.0, std=v_std)  # 跟上面nn.init.normal_的效果一样

        # selfAttention Layer
        temperature = np.power(q_k_out_dim, 0.5)
        self.attention = SelfAttentionLayer(temperature,
                                            self_attention_dropout)  ## [batch_size, seq_len, num_head * v_out_dim]

        # 最后进行全连接降维，因为后面会有多层MultiHeadAttentionLayer,所以降维的维度要保持和MultiHeadAttentionLayer的输入维度一样：即为embedding_dim
        self.fc = nn.Linear(num_head * v_out_dim, embedding_dim)
        nn.init.xavier_normal_(self.fc.weight)  # 权重初始化

        self.dropout = nn.Dropout(multi_attention_dropout)

        # 最后的输出要做下norm
        self.layer_norm = nn.LayerNorm(embedding_dim)

    def forward(self, input_q, input_k, input_v, mask=None):
        """
        一般情况下的input_q，input_k,input_v三者是一样的在最开始就是word_embedding+position_embedding之后的源语言的数据；后面就是每层EncoderLayer的输出
        :param input_q:  [batch_size,batch_seq_q_len,embedding_dim]：注意这个batch_seq_q_len不需要和batch_seq_k_v_len一致，
        因为在decoder的第二层MultiHeadAttentionLayer的时候batch_seq_q_len是目标语言的句子长度，batch_seq_k_v_len是源语言的句子长度
        :param input_k: [batch_size,batch_seq_k_v_len,embedding_dim]：batch_seq_k_v_len：k，v的句子长度必须一致
        :param input_v: [batch_size,batch_seq_k_v_len,embedding_dim]
        :param mask: [batch_size,batch_seq_q_len,batch_seq_k_v_len] :为0的位置是要保留的注意力权重，为1的是要mask掉的
        :return: [batch_size,batch_seq_q_len,embedding_dim] 加上了多个head方式的的self-Attention之后的value值：
                输出之所以后面的维度为embedding_dim，是为了后面进行多层的EncoderLayer(当然embedding_dim也可以做一层全连接降维)
        """
        assert input_q.size(2) == input_k.size(2) and input_k.size(1) == input_v.size(1)  # size相同
        batch_size = input_q.size()[0]
        batch_seq_q_len = input_q.size(1)  # 注意这里必须是q的句子长度
        batch_seq_k_v_len = input_k.size(1)  # 这里是k,v的句子长度
        q_k_out_dim = self.q_k_out_dim
        v_out_dim = self.v_out_dim
        num_head = self.num_head

        # 原始的输入：在第一次的时候就是word_embedding+position_embedding之后的源语言/目标语言的数据；后面就是每层EncoderLayer的输出
        # 这个input_original必须是q；因为在decoder的第二层MultiHeadAttentionLayer时q与目标语言，k，v是encoder的输出
        input_original = input_q  # [batch_size,batch_seq_q_len,embedding_dim]

        # 计算q:这里的句子长度是:batch_seq_q_len
        # 首先进过全连接计算出MultiHead的q矩阵：output的size: [batch_size, batch_seq_q_len,num_head,q_k_out_dim]
        q = self.w_q(input_q).view(batch_size, batch_seq_q_len, num_head,
                                   q_k_out_dim)  # [batch_size, batch_seq_q_len,num_head,q_k_out_dim]
        # 将计算出的q进行size形状的调整,调整后的output的size：# [(num_head* batch_size),batch_seq_q_len,q_k_out_dim]
        # contiguous()是为了把进过permute操作后物理地址不连续的tensor的物理地址重写变成连续的，以加速和方便后面的运算
        q = q.permute(2, 0, 1, 3).contiguous().view(-1, batch_seq_q_len,
                                                    q_k_out_dim)  # [num_head * batch_size,batch_seq_q_len,q_k_out_dim]

        # 同上计算出k ： 这列的句子长度是：batch_seq_k_v_len
        k = self.w_k(input_k).view(batch_size, batch_seq_k_v_len, num_head,
                                   q_k_out_dim)  # [batch_size,batch_seq_k_v_len,num_head,q_k_out_dim]
        k = k.permute(2, 0, 1, 3).contiguous().view(-1, batch_seq_k_v_len,
                                                    q_k_out_dim)  # [num_head * batch_size, batch_seq_k_v_len,q_k_out_dim]

        # 同上计算出v： 这列的句子长度是：batch_seq_k_v_len
        v = self.w_v(input_v).view(batch_size, batch_seq_k_v_len, num_head,
                                   v_out_dim)  # [batch_size,batch_seq_k_v_len,num_head,v_out_dim]
        v = v.permute(2, 0, 1, 3).contiguous().view(-1, batch_seq_k_v_len,
                                                    v_out_dim)  # [num_head * batch_size,batch_seq_k_v_len,v_out_dim]

        # 对mask的Tensor进行num_head的repeat操作:维度0 repeat上num_head次，其他维度不repeat
        mask = mask.repeat(num_head, 1, 1)  # [num_head * batch_size, batch_seq_q_len, batch_seq_k_v_len]
        # 计算出self-Attention的value值 和 Attention矩阵
        # output:[num_head * batch_size,batch_seq_q_len,v_out_dim]
        # attention : [num_head * batch_size,batch_seq_q_len,batch_seq_k_v_len]
        output, attention = self.attention(q, k, v, mask=mask)

        # 把output的维度进行调整，使其最终size为:[batch_size,batch_seq_q_len,num_head * v_out_dim]
        output = output.view(num_head, batch_size, batch_seq_q_len,
                             v_out_dim)  # [num_head , batch_size,batch_seq_q_len,v_out_dim]
        output = output.permute(1, 2, 0, 3).contiguous().view(batch_size, batch_seq_q_len,
                                                              -1)  # [batch_size,batch_seq_q_len,num_head * v_out_dim]

        # 进行全连接操作，进行降维
        output = self.dropout(self.fc(output))  # [batch_size,batch_seq_q_len,embedding_dim]

        # 这个把原始的数据加上相当于残差项目，这样即使层数很多也能保证不出现信息过少导致的梯度消失问题
        output = output + input_original  # [batch_size,batch_seq_q_len,embedding_dim]

        # 最后要把输出做做下norm
        output = self.layer_norm(output)  # [batch_size,batch_seq_q_len,embedding_dim]

        return output, attention


class FeedForwardLayer(nn.Module):
    # 在每一层的EncoderLayer或者DecoderLayer最后都要把提炼好的词向量信息(维度为：embedding_dim)扩大(论文中是4倍)后用Relu激活，
    # 然后在把dim还原回embedding_dim，接着在进行norm操作：
    # 这样做的目的：在更大的空间向量中，可以跟方便的提取需要的信息；
    # 对应公式为：FFN(x) = ReLU(xW1+b1)W2+b2
    def __init__(self, embedding_dim, intermediate_dim, ff_dropout=0.1):
        """
        :param embedding_dim:
        :param intermediate_dim: 中点一个更大维度的中转层维度
        :param ff_dropout:
        """
        super(FeedForwardLayer, self).__init__()
        self.w_1 = nn.Linear(embedding_dim, intermediate_dim)
        self.w_2 = nn.Linear(intermediate_dim, embedding_dim)

        self.dropout = nn.Dropout(ff_dropout)

        self.layer_norm = nn.LayerNorm(embedding_dim)

    def forward(self, x):
        """
        :param x: [batch_size,batch_seq_len,embedding_dim]
        :return:
        """
        # 计算公式：FFN(x) = ReLU(xW1+b1)W2+b2

        # 记录残差项
        residual = x  # [batch_size,batch_seq_len,embedding_dim]

        # 先进行扩维度
        output = self.w_1(x)  # [batch_size,batch_seq_len,intermediate_dim]

        # relu激活
        output = torch.nn.functional.relu(output)  # [batch_size,batch_seq_len,intermediate_dim]

        # 在把维度还原
        output = self.w_2(output)  # [batch_size,batch_seq_len,embedding_dim]

        # dropout
        output = self.dropout(output)  # [batch_size,batch_seq_len,embedding_dim]

        # 把output与残差项residual相加之后再进行 norm
        output = self.layer_norm(output + residual)

        return output


# </editor-fold>

# =========================================================<editor-fold des="DecoderModel相关">=========================================================
class EncoderLayer(nn.Module):
    """
    在word embedding + pos embedding之后的size为[batch_size,batch_seq_len,embedding_size]的tensor作为输入
    通过EncoderLayer 最终输出 []
    """

    def __init__(self, num_head, embedding_dim, q_k_out_dim, v_out_dim,
                 ff_intermediate_dim,
                 multi_attention_dropout=0.1,
                 self_attention_dropout=0.1,
                 ff_dropout=0.1):
        super(EncoderLayer, self).__init__()

        # 首先进行MultiHeadAttention得到加了不同注意力的信息之后的每个词的value
        # output：[batch_size,batch_seq_len,embedding_dim]; attention:[num_head*batch_size,batch_seq_len,embedding_dim]
        self.multi_attention = MultiHeadAttentionLayer(num_head, embedding_dim, q_k_out_dim, v_out_dim,
                                                       multi_attention_dropout, self_attention_dropout)

        self.feed_forward = FeedForwardLayer(embedding_dim, ff_intermediate_dim, ff_dropout)

    def forward(self, encoder_layer_input, self_attention_mask=None, non_pad_mask=None):
        """

        :param encoder_layer_input:
        :param self_attention_mask: 在Attention的时候需要mask的词的信息：[batch_size,batch_seq_len,embedding_dim]:注意需要mask的地方为1，不需要mask的为0
        :param non_pad_mask: 防止pad位置有信息输出：[batch_size,batch_seq_len,1]；注意是pad的地方为0，不是pad的地方为1
        :return: [batch_size，batch_seq_len,embedding_size] encoder之后的信息
        """
        input_q = encoder_layer_input
        input_k = encoder_layer_input
        input_v = encoder_layer_input

        # multi_attention_output:[batch_size,batch_seq_len,embedding_dim]
        # multi_attention:[num_head * batch_size,batch_seq_len,batch_seq_len]
        multi_attention_output, multi_attention = self.multi_attention(input_q, input_k, input_v, self_attention_mask)
        # 防止pad位置的信息输出，让pad位置的信息输出始终为0
        multi_attention_output *= non_pad_mask  # [batch_size,batch_seq_len,embedding_size]

        # 进行feed_forward操作
        feed_forward_output = self.feed_forward(multi_attention_output)  # [batch_size,batch_seq_len,embedding_size]
        # 再次过滤掉pad位置的信息
        feed_forward_output *= non_pad_mask

        return feed_forward_output, multi_attention


class EncoderModel(nn.Module):
    """
    Encoder 模型:负责进行源语言的Encode处理
    """

    def __init__(self, num_vocab_size, max_seq_len, embedding_dim, num_encoder_layers, num_head,
                 q_k_out_dim, v_out_dim,
                 ff_intermediate_dim,
                 use_absolute_position=False,
                 multi_attention_dropout=0.1,
                 self_attention_dropout=0.1,
                 ff_dropout=0.1):
        """
        :param num_vocab_size: one-hot的词表大小
        :param embedding_dim: 词嵌入的维度embedding_dim,也是隐藏层的维度hidden_size
        :param max_seq_len: 注意这里的max_seq_len不是指的batch中最长的句子长度，而是用户传入的一个超参数：最长允许的句子长度
        :param num_encoder_layers: 需要多少层encoder_layer
        :param num_head: 每一层encoder_layer的multi_head的数目：每一个对应提取一种Attention信息
        :param q_k_out_dim: q、k矩阵的输出维度，他们两个的输出维度必须一致
        :param v_out_dim: v的输出维度，不需要和q、k的输出维度一致；最后self-Attention的时候会把num_head * v_out_dim做一次全连接变为hidden_size = embedding_dim
        :param ff_intermediate_dim: 在feed forward的时候中间扩维层的维数
        :param use_absolute_position: 是否使用绝对位置编码：默认不使用
        :param multi_attention_dropout: multi_attention的输出时的dropout比例：默认0.1
        :param self_attention_dropout: self_attention的输出时的dropout比例: 默认0.1
        :param ff_dropout: feed forward输出的时的dropout比例: 默认0.1
        """
        super(EncoderModel, self).__init__()

        # 首先进行word embedding操作:num_vocab_size:one-hot词表的个数，embedding_size：需要embedding表示的维数，
        # padding_idx：在one-hot中占位符PAD的one-hot值，给定的话将会始终将PAD的embedding表示的权重始终置为零
        # input_size:[batch_size,batch_seq_length];  output_size:[batch_size,batch_seq_length,embedding_dim]
        self.word_embedding = nn.Embedding(num_vocab_size, embedding_dim, padding_idx=dataset.PAD)

        # position embedding
        # 注意这里的max_seq_len不是指的batch中最长的句子长度，而是用户传入的一个超参数：最长允许的句子长度
        # 它可以是所有源语言中句子最长的那个句子长度(加上开启和结束以及其他标志的句子长度)，也可以是源语言和目标语言中所有句子中最长的长度，或者是比他们更大的数(取决于正式翻译场景中的值，或者是性能较优的值)
        # input_size:[batch_size,batch_seq_length]; output_size:[batch_size,batch_seq_length,embedding_dim]
        if use_absolute_position:  # 使用绝对位置编码: 虽然是绝对位置编码，但是embedding的值任然是要梯度下降来调整的
            self.position_embedding = nn.Embedding(max_seq_len, embedding_dim, padding_idx=dataset.PAD_POSITION)
        else:  # 使用相对位置编码：虽然是相对位置编码，单这个是通过人为设计的原则来计算每一个位置的embedding值的，不需要通过梯度下降来调整
            self.position_embedding = nn.Embedding.from_pretrained(
                get_sinusoid_embedding_position_matrix(max_seq_len, embedding_dim, padding_idx=dataset.PAD_POSITION),
                freeze=True)

        # 下面就要进行多层的EncoderLayer
        self.encoder_layers = nn.ModuleList([
            EncoderLayer(num_head, embedding_dim, q_k_out_dim, v_out_dim,
                         ff_intermediate_dim,
                         multi_attention_dropout,
                         self_attention_dropout,
                         ff_dropout)
            for _ in range(num_encoder_layers)
        ])

    def forward(self, source_seq, source_position, return_attentions=False):
        """
        Encoder 前向传播
        :param source_seq: [batch_size,batch_seq_len] : 每个词都是one-hot的数字
        :param source_position: [batch_size,batch_seq_len] : 每个位置上都是绝对的位置信息
        :param return_attentions: 是否返回Encoder的每一层的EncoderLayer的Attention组成的list
        :return:
        """
        # 初始化一个list用来存放每一层的attention
        attention_list = []

        # 初始化encoder_layer需要的参数：
        self_attention_mask = get_self_attention_q_k_pad_mask(seq_q=source_seq,
                                                              seq_k=source_seq)  # [batch_size,batch_seq_len,batch_seq_len]
        non_pad_mask = get_non_pad_mask(source_seq)  # [batch_size,batch_seq_len,1]

        # 加词embedding和位置embedding的输出相加，构成最初始的第0层EncoderLayer的输入
        # encoder_layer_input:[batch_size,batch_seq_len,embedding_dim]
        encoder_layer_output = self.word_embedding(source_seq) + self.position_embedding(source_position)

        # 进行多层的encoder
        for encoder_layer in self.encoder_layers:
            # encoder_layer_input:[batch_size,batch_seq_len,embedding_dim]
            # attention:[num_head * batch_size,batch_seq_len,batch_seq_len]
            encoder_layer_output, attention = encoder_layer(encoder_layer_output,
                                                            self_attention_mask=self_attention_mask,
                                                            non_pad_mask=non_pad_mask)
            if return_attentions:
                attention_list.append(attention)

        if return_attentions:
            return encoder_layer_output, attention_list

        return encoder_layer_output


# </editor-fold>

# =========================================================<editor-fold des="DecoderModel相关">=========================================================
class DecoderLayer(nn.Module):
    """
    DecoderLayer
    """

    def __init__(self, num_head, embedding_dim, q_k_out_dim, v_out_dim,
                 ff_intermediate_dim,
                 multi_attention_dropout=0.1,
                 self_attention_dropout=0.1,
                 ff_dropout=0.1):
        super(DecoderLayer, self).__init__()

        # 第一层MultiHeadAttentionLayer：
        # 这一层采用的是decode的input进行的self-attention：
        # 采用的是用上三角矩阵(主对角线以下全为0，其余位置为1)mask了target的embedding输出后再进行的所有位置的并行self-attention：
        # 保证了每一个位置预测的下一个词的时候都只能看之前已经翻译出来的词(因为训练的时候需要之前看前面正确的词来预测，这样才能保证并行；真实翻译的时候是不能并行的，只能一个个的预测)
        # 它所接受到的q，k，v就是：target语言加上mask预测值之后信息的embedding后的结果
        self.decoder_multi_attention = MultiHeadAttentionLayer(num_head, embedding_dim, q_k_out_dim, v_out_dim,
                                                               multi_attention_dropout=multi_attention_dropout,
                                                               self_attention_dropout=self_attention_dropout)

        # 第二层MultiHeadAttentionLayer：
        # 这一层是为了把encoder输出的信息加入进来：相当于传统的decoder时引入输入的attention机制，也是一种用源语言信息知道翻译的一种有效手段
        # 他的q是target语言mask之后的embedding结果，k,v是encoder模型的输出
        # 注意这里的target_seq_len与source_seq_len并不相同，也不需要相同，只要保证q,k的embedding_dim相同，k,v的seq_len相同即可
        # q 的size为:[batch_size,batch_target_seq_len,embedding_dim]
        # k 的size为:[batch_size,batch_source_seq_len,embedding_dim]
        # v 的size为:[batch_size,batch_source_seq_len,embedding_dim]
        self.decoder_encoder_multi_attention = MultiHeadAttentionLayer(num_head, embedding_dim, q_k_out_dim, v_out_dim,
                                                                       multi_attention_dropout=multi_attention_dropout,
                                                                       self_attention_dropout=self_attention_dropout)

        # feed_forward层:信息扩维之后提取信息在降维
        self.feed_forward = FeedForwardLayer(embedding_dim, ff_intermediate_dim, ff_dropout)

    def forward(self, decoder_layer_input, encoder_output, self_attention_mask=None, non_pad_mask=None,
                decoder_encoder_attention_mask=None):
        '''
        :param decoder_layer_input: 目标语言embedding(word+position)之后输入 [batch_size,batch_target_seq_len,embedding_dim]
        :param encoder_output: encoder模型的输出:[batch_size,batch_source_seq_len,embedding_dim]
        :param self_attention_mask: 目标语言的针对目标语言自身的self_attention_mask:[batch_size,batch_target_seq_len,batch_target_seq_len]
        :param non_pad_mask: attention操作后把pad位置的输出置为0的mask：[batch_size,batch_target_seq_len,1]
        :param decoder_encoder_attention: 目标语言的针对源语言的attention_mask: [batch_size,batch_target_seq_len,batch_source_seq_len]
        :return: DecoderLayer的最终输出：[batch_size,batch_target_seq_len,embedding_dim]
        '''
        # 目标语言对目标语言自身的注意力
        # decoder_output:[batch_size,batch_target_seq_len,embedding_dim]
        # decoder_multi_attention:[num_head * batch_size,batch_target_seq_len,batch_target_seq_len]
        decoder_output, decoder_multi_attention = self.decoder_multi_attention(input_q=decoder_layer_input,
                                                                               input_k=decoder_layer_input,
                                                                               input_v=decoder_layer_input,
                                                                               mask=self_attention_mask)
        # decoder_layer_input *= non_pad_mask  # [batch_size,batch_target_seq_len,embedding_dim] 这是一个严重错误，在使用完之后根本就没有再次对他进行使用,此时的改变会影响反向出传播
        decoder_output *= non_pad_mask  # [batch_size,batch_target_seq_len,embedding_dim]

        # 目标语言对源语言的注意力
        # decoder_output：[batch_size,batch_target_seq_len,embedding_dim]
        # decoder_encoder_attention: [num_head * batch_size,batch_target_seq_len,batch_source_seq_len]
        decoder_output, decoder_encoder_attention = self.decoder_encoder_multi_attention(input_q=decoder_output,
                                                                                         input_k=encoder_output,
                                                                                         input_v=encoder_output,
                                                                                         mask=decoder_encoder_attention_mask)
        decoder_output *= non_pad_mask  # [batch_size,batch_target_seq_len,embedding_dim]

        # 最后在进过feed forward操作：先升维提取信息，然后在降维会embedding_dim
        decoder_output = self.feed_forward(decoder_output)  # [batch_size,batch_target_seq_len,embedding_dim]
        decoder_output *= non_pad_mask  # [batch_size,batch_target_seq_len,embedding_dim]

        return decoder_output, decoder_multi_attention, None


class DecoderModel(nn.Module):
    """
    Decoder 模型:负责进行目标语言的Decoder处理
    """

    def __init__(self, num_vocab_size, max_seq_len, embedding_dim, num_decoder_layers, num_head,
                 q_k_out_dim, v_out_dim,
                 ff_intermediate_dim,
                 use_absolute_position=False,
                 multi_attention_dropout=0.1,
                 self_attention_dropout=0.1,
                 ff_dropout=0.1):
        super(DecoderModel, self).__init__()

        # word embedding:
        self.word_embedding = nn.Embedding(num_vocab_size, embedding_dim, padding_idx=dataset.PAD)

        # position embedding:
        if use_absolute_position:  # 使用可训练的绝对位置编码
            self.position_embedding = nn.Embedding(max_seq_len, embedding_dim, padding_idx=dataset.PAD_POSITION)
        else:
            self.position_embedding = nn.Embedding.from_pretrained(
                get_sinusoid_embedding_position_matrix(max_seq_len, embedding_dim, padding_idx=dataset.PAD_POSITION),
                freeze=True)

        # 多层的decoder_layer
        self.decoder_layers = nn.ModuleList([
            DecoderLayer(num_head, embedding_dim, q_k_out_dim, v_out_dim,
                         ff_intermediate_dim,
                         multi_attention_dropout,
                         self_attention_dropout,
                         ff_dropout)
            for _ in range(num_decoder_layers)
        ])

    def forward(self, target_seq, target_position, source_seq, encoder_output, return_attentions=False):
        """

        :param target_seq: 目标语言one-hot词信息信息：[batch_size,batch_target_seq_len]
        :param target_position: 目标语言one-hot位置信息: [batch_size,batch_target_seq_len]
        :param source_seq: 源语言的one-hot词信息为了计算目标语言对源语言的PAD位置的mask:[batch_size,batch_source_seq_len]
        :param encoder_output: encoder层的输出[batch_size,batch_source_seq_len,embedding_dim]
        :param return_attentions: 是否返回attention信息
        :return: decoder的输出
        """
        # 创建存放目标语言对目标源语言的attention数据的列表；目标语言对encoder_output的attention数据的列表
        decoder_self_attention_list = []
        decoder_encoder_attention_list = []

        # 初始化decoder过程中重要的一些参数
        # decoder对目标语言自身的mask：既不能注意PAD位置的词，也不能注意预测词后面的词
        # 对target自身PAD位置的词不能去注意
        self_attention_pad_mask = get_self_attention_q_k_pad_mask(target_seq,
                                                                  target_seq)  # [batch_size,batch_target_seq_len,batch_target_seq_len]
        # 对预测词及后面的词也不能去注意：不去看后面
        self_attention_do_not_see_subsequent_mask = get_do_not_see_subsequent_mask(
            target_seq)  # [batch_size,batch_target_seq_len,batch_target_seq_len]
        # self_attention_pad_mask + self_attention_do_not_see_subsequent_mask为零的地方说明双方都不需要mask，没有问题
        # 为1的地方说明有一方要mask也没有问题；为2的地方说明两边都要mask:这时候就要把它变回1了，不然就不会mask了
        # gt(0)操作就是把为0的地方变为False，不为0的地方变为True；false的地方不mask，True的地方要mask这样就没问题了
        self_attention_mask = (self_attention_pad_mask + self_attention_do_not_see_subsequent_mask).gt(0)

        # 目标语言自身pad的mask
        non_pad_mask = get_non_pad_mask(target_seq)  # [batch_size,batch_target_seq_len,1]

        # decoder对encoder_output的mask：即为目标语言对源语言的mask，不用注意源语言的PAD位置
        # 注意这里用的是source_seq
        decoder_encoder_attention_mask = get_self_attention_q_k_pad_mask(target_seq, source_seq)

        # 将目标语言的word_embedding 信息+ position_embedding信息作为decoder的原始输入
        decoder_layer_output = self.word_embedding(target_seq) + self.position_embedding(target_position)

        for decoder_layer in self.decoder_layers:
            decoder_layer_output, decoder_multi_attention, decoder_encoder_attention = decoder_layer(
                decoder_layer_output,
                encoder_output,
                self_attention_mask=self_attention_mask,
                non_pad_mask=non_pad_mask,
                decoder_encoder_attention_mask=decoder_encoder_attention_mask)
            if return_attentions:
                decoder_self_attention_list.append(decoder_multi_attention)
                decoder_encoder_attention_list.append(decoder_encoder_attention)

        if return_attentions:
            return decoder_layer_output, decoder_self_attention_list, decoder_encoder_attention_list
        return decoder_layer_output

    # </editor-fold>
