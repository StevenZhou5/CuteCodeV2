# 943. 最短超级串
# 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。
#
# 我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。
#
#
# 
# 示例 1：
#
# 输入：words = ["alex","loves","leetcode"]
# 输出："alexlovesleetcode"
# 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
# 示例 2：
#
# 输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# 输出："gctaagttcatgcatc"
#
#
# 提示：
#
# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] 由小写英文字母组成
# words 中的所有字符串 互不相同

class Solution():
    def get_min_sub_str_dp_sc(self, words):
        # 状态定义，dp[(state,idx)] 在选取了state中的单词后并且以words[idx]结尾时最小的单位长度
        # 假设有五个单词： state = 11001 代表选了第一个，第四个 和 第 五个单词 组成的字符串的最小长度
        dp = {}
        n = len(words)
        final_state = (1 << n) - 1
        self.res = None

        def recursion(cur_state, cur_end_idx, cur_str):
            if cur_state == final_state:
                dp[(cur_state, cur_end_idx)] = cur_str
                self.res = cur_str if not self.res or len(self.res) > len(cur_str) else self.res
                return
            if (cur_state, cur_end_idx) in dp and len(cur_str) >= len(dp[(cur_state, cur_end_idx)]):
                return
            dp[(cur_state, cur_end_idx)] = cur_str
            for i in range(n):
                i_state = 1 << i
                if i_state & cur_state != 0:  # i 位置的词已经被选了
                    continue
                # 把word[i] 拼到 cur_str后面尽可能复用末尾的值
                cur_word = words[i]
                target_idx = len(cur_str) - len(cur_word)
                target_idx = 0 if target_idx < 0 else target_idx
                new_str = ""
                for split_idx in range(target_idx, len(cur_str) + 1):
                    if cur_word.startswith(cur_str[split_idx:]):  #
                        new_str = cur_str[:split_idx] + cur_word
                        break
                new_state = cur_state + i_state
                recursion(new_state, i, new_str)

        recursion(0, -1, "")
        print(dp)
        return self.res


solu = Solution()
# words = ["alex", "loves", "leetcode"]
words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
print("res:", solu.get_min_sub_str_dp_sc(words))
