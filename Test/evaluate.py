import sys, getopt
import tensorflow as tf
import pandas as pd
from sklearn.metrics import roc_auc_score


def evaluate(model_file_path, evaluate_data_file_path,top_order_index,is_evaluate_base = False,pred_only=True):
    tag_name = "serve"
    signature_key = "byway_dcn"
    target_columns_name = ["label"]
    final_rank_columns_name = ["final_rank"]
    other_columns_name = ["route_id"]
    order_index_name = "order_index" # 列名：此列的值用于表示此条订单所在的推荐列表中的位置
    predict_column_name = "predict"
    with tf.Session(graph=tf.Graph()) as sess:
        # step1：加载模型graph
        meta_graph_def = tf.saved_model.loader.load(sess, [tag_name], model_file_path)

        # step2：从meta_graph_def中取出SignatureDef对象
        signature = meta_graph_def.signature_def

        # step3：从signature获取所有输入与输出的inputs 与 outputs的key值
        inputs_name = []
        for key in signature[signature_key].inputs:
            inputs_name.append(key)

        outputs_name = []
        for key in signature[signature_key].outputs:
            outputs_name.append(key)

        # step4：取出待评测的输入
        inputs_columns_name = [tensor_name[:-4] for tensor_name in inputs_name]
        evaluate_data_df = pd.read_csv(evaluate_data_file_path,
                                       usecols=inputs_columns_name + other_columns_name + target_columns_name + final_rank_columns_name + [order_index_name])
        if top_order_index > 0:
            evaluate_data_df = evaluate_data_df[evaluate_data_df[order_index_name] <= top_order_index]

        # step5：构建模型需要的输入,输入 tensor
        inputs_dict = {}
        for key in inputs_name:
            # 获取tensor
            tensor = sess.graph.get_tensor_by_name(key)

            # 将对应key值的所有输入以列表的形式组合，并赋值给inputs_dict
            inputs_dict[tensor] = evaluate_data_df[key[:-4]].values.reshape((-1, 1))

        outputs_list = []
        for key in outputs_name:
            # 获取tensor
            tensor = sess.graph.get_tensor_by_name(key)

            # 输出的tensor并不需要是dict，因为他们不需要值
            outputs_list.append(tensor)
        res = sess.run(outputs_list, inputs_dict)
    evaluate_data_df[predict_column_name] = res[0]

    if pred_only:
       print(res[0])
       return

    auc_score = round(roc_auc_score(evaluate_data_df[target_columns_name].values,
                                    evaluate_data_df[predict_column_name].values), 4)  # 必须正负样本都有才可以,计算最终AUC
    print("最终评测数据的AUC：%s" % (auc_score))
    
    groups = evaluate_data_df.groupby(['route_id'])
    all_count = groups['label'].max().sum() # 代表所有被邀请的订单总数
    
    def get_pre_top3_complete_count(group):
        top3 = group[1].sort_values([predict_column_name],ascending=False).head(3)
        return max(top3.label.values)
    pre_top3_count = sum(list(map(get_pre_top3_complete_count,groups)))
    pre_top3_rate = pre_top3_count / all_count
    pre_top1 = groups.apply(lambda x:x.sort_values([predict_column_name],ascending=False).head(1))
    pre_top1_count = len(pre_top1[pre_top1.label==1])
    pre_top1_rate = pre_top1_count / all_count
    print("最终模型预测完单数统计:all_count=%d;top3_count=%d;top1_count=%d"%(all_count,pre_top3_count,pre_top1_count)) 
    print("最终模型预测完单占比统计:top3_rate=%.4f;top1_rate=%.4f"%(pre_top3_rate,pre_top1_rate))
    
    if is_evaluate_base:
        final_rank_auc_score = round(roc_auc_score(evaluate_data_df[target_columns_name].values,
                                               evaluate_data_df[final_rank_columns_name].values),
                                 4)
        print("final_rank的AUC：%s" % (final_rank_auc_score))
        
        def get_top3_complete_count(group):
            top3 = group[1].sort_values(final_rank_columns_name,ascending=False).head(3)
            return max(top3.label.values)
        top3_count = sum(list(map(get_top3_complete_count,groups)))
        top3_rate = top3_count / all_count
        top1 = groups.apply(lambda x:x.sort_values(final_rank_columns_name,ascending=False).head(1))
        top1_count = len(top1[top1.label==1])
        top1_rate = top1_count / all_count
        print("final_rank完单数统计:all_count=%d;top3_count=%d;top1_count=%d"%(all_count,top3_count,top1_count)) 
        print("final_rank完单占比统计:top3_rate=%.4f;top1_rate=%.4f"%(top3_rate,top1_rate))
    

def main(argv):
    # model_file_path = "../model/beijing/modelv1_2_3/model/"
    # evaluate_data_file_path = "/home/odin/stevenzhouzhenwu/dcn/data/city1/v1_2_3/oot.csv_norm"
    model_file_path = ""
    evaluate_data_file_path = ""
    top_order_index = -1 # -1代表评测所有位置，位置索引是从1开始计数的，所以输入值必须是大于0的值
    try:
        opts, args = getopt.getopt(argv, "hm:e:t:", ["model_file_path=", "evaluate_data_file_path=","top_order_index="])
    except getopt.GetoptError:
        print("evaluate.py -m <model_file_path> -e <evaluate_data_file_path> -t <top_order_index>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("evaluate.py -m <model_file_path> -e <evaluate_data_file_path> -t <top_order_index>")
            sys.exit()
        elif opt in ('-m', '--model_file_path'):
            model_file_path = arg
        elif opt in ('-e', '--evaluate_data_file_path'):
            evaluate_data_file_path = arg
        elif opt in ('-t', '--top_order_index'):
            top_order_index = int(arg)
    print("模型文件路径：%s" % (model_file_path))
    print("待评测的归一化数据文件：%s" % (evaluate_data_file_path))
    print("评测top_order_index：%s"%(top_order_index))
    if model_file_path == "" or evaluate_data_file_path == "":
        print("evaluate.py -m <model_file_path> -e <evaluate_data_file_path> -t <top_order_index>")
        sys.exit()
    evaluate(model_file_path, evaluate_data_file_path, top_order_index)
    print("evaluate DONE!")


if __name__ == '__main__':
    main(sys.argv[1:])
