# 面试题 17.13. 恢复空格
# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
# 像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
# 在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
# 假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
#
# 注意：本题相对原题稍作改动，只需返回未识别的字符数
#
#
#
# 示例：
#
# 输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
# 提示：
#
# 0 <= len(sentence) <= 1000
# dictionary中总字符数不超过 150000。
# 你可以认为dictionary和sentence中只包含小写字母。

class Solution():

    def get_res_with_rkhash(self, dictionary, sentence):
        # rabin-karp 拉宾-卡普算法：base进制的字符串表示法 + 滚动增加计算；再加上质数取模；
        # hash算法： 找一个base ，利用base进制表示一段字符串
        # 例如 假设base = 3， 字符a=0 ; 字符b=1; 字符c=2;
        # 那么 abca = 1231 的三进制数，转换为十进制= 1*(3^0) + 3*(3^1) + 2*(3^2) + 1 *(3^3) =

        # 核心 base 值 (至少要大于所有字符种类的数目，比如字符串中总共有26种字符，那么base至少要大于26)，
        # 用于取模的 mod 值，最好选用质数，且 要大于字典容量值，比如总购有100个词，那么mod必须要大于100 ，不然就容易产生hash冲突，而且最好远大于字典容量

        # ord('a') = 97 ,做一我们要求一个字符的base进制的数 = ord(chr) - 96
        base = 30
        mod = 999983
        dictionary_hash_map = {}
        for word in dictionary:
            hash_val = 0
            for i in range(len(word) - 1, -1, -1):  # 要倒着存，方便后面sentence的hash值计算
                hash_val = ((hash_val * base) % mod + (ord(word[i]) - 96)) % mod
            dictionary_hash_map[hash_val] = word
        print(dictionary_hash_map)

        n = len(sentence)
        dp = [0] * n  # 截止到当前位置的字符，最少未识别的字符数

        for i in range(n):
            cur_hash_val = 0
            cur_dp = float('inf')
            for j in range(i, -1, -1):
                cur_hash_val = ((cur_hash_val * base) % mod + (ord(sentence[j]) - 96)) % mod
                dp_pre = dp[j - 1] if j > 0 else 0
                cur_dp = min(dp_pre + (0 if cur_hash_val in dictionary_hash_map else i - j + 1), cur_dp)
            dp[i] = cur_dp
        print(dp)
        return dp[-1]

    def get_res_with_trie(self, dictionary, sentence):
        class Trie():
            def __init__(self):
                self.Next = [None for _ in range(26)]
                self.is_end = False

        trie_root = Trie()
        for word in dictionary:
            cur_trie = trie_root
            for i in range(len(word) - 1, -1, -1):
                idx = ord(word[i]) - 97
                if not cur_trie.Next[idx]:
                    cur_trie.Next[idx] = Trie()
                cur_trie = cur_trie.Next[idx]
            cur_trie.is_end = True

        # from collections import deque
        # queue = deque()
        # queue.append(trie_root)
        # level = 1
        # while queue:
        #     print("第%d层:" % (level))
        #     level += 1
        #     for i in range(len(queue)):
        #         cur = queue.pop()
        #         print(cur.Next, cur.is_end)
        #         for next_trie in cur.Next:
        #             if next_trie:
        #                 queue.append(next_trie)

        n = len(sentence)
        dp = [0] * n
        for i in range(n):
            cur_trie = trie_root
            cur_dp = float('inf')
            for j in range(i, -1, -1):
                cur_trie = cur_trie.Next[ord(sentence[j]) - 97]
                pre_dp = dp[j - 1] if j > 0 else 0
                if not cur_trie:  # 如果后缀已经不存在，直接返回
                    cur_dp = min(cur_dp, pre_dp + i - j + 1)
                    break
                if cur_trie.is_end:  # 如果当前后缀是一个完整单词
                    cur_dp = min(cur_dp, pre_dp)
                else:
                    cur_dp = min(cur_dp, pre_dp + i - j + 1)
            dp[i] = cur_dp
        print(dp)
        return dp[-1]


solu = Solution()
dictionary = ["looked", "just", "like", "her", "brother"]
sentence = "jesslookedjustliketimherbrother"
# dictionary = ['a', 'sdsa']
# sentence = "sdsa"
# print("res:", solu.get_res_with_rkhash(dictionary, sentence))
print("res:", solu.get_res_with_trie(dictionary, sentence))
