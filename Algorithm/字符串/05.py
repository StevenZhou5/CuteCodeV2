# 5. 最长回文子串
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
#
# 输入：s = "a"
# 输出："a"
# 示例 4：
# 
# 输入：s = "ac"
# 输出："a"
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母（大写和/或小写）组成

class Solution():
    def get_max_substr_with_center_expand(self, s):
        n = len(s)

        def center_expand(left_idx, right_idx):
            while 0 < left_idx <= right_idx < n - 1 and s[left_idx - 1] == s[right_idx + 1]:
                left_idx -= 1
                right_idx += 1
            return (left_idx, right_idx, right_idx - left_idx + 1)

        res_left_idx = 0
        res_right_idx = 0
        res_len = 1
        for i in range(n):
            cur_left_idx, right_idx, cur_len = center_expand(i, i)
            if cur_len > res_len:
                res_left_idx, res_right_idx, res_len = cur_left_idx, right_idx, cur_len
            if i < n - 1 and s[i] == s[i + 1]:
                cur_left_idx, right_idx, cur_len = center_expand(i, i + 1)
                if cur_len > res_len:
                    res_left_idx, res_right_idx, res_len = cur_left_idx, right_idx, cur_len

        return s[res_left_idx:res_right_idx + 1]

    def get_max_substr_with_dp(self, s):
        n = len(s)
        # 状态定义：dp[i][j] 代表从s的第i个字符到s的第j个字符是否是回文子串
        dp = [[True if i == j else False for j in range(n)] for i in range(n)]

        max_len = 0
        max_left_idx = 0
        max_right_idx = 0
        # 注意遍历的方式要从斜对角线的每个位置从下想上遍历
        for col in range(1, n):
            for row in range(col - 1, -1, -1):  #
                if s[row] != s[col]:
                    dp[row][col] = False
                else:
                    dp[row][col] = dp[row + 1][col - 1] if col - row > 1 else True
                    if dp[row][col] and col - row > max_len:
                        max_len, max_left_idx, max_right_idx = col - row, row, col

        return s[max_left_idx:max_right_idx + 1]


solu = Solution()
s = "ccbacc"
print("res:", solu.get_max_substr_with_center_expand(s))
print("res:", solu.get_max_substr_with_dp(s))
