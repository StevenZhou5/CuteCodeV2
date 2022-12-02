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
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        # 时间复杂度： O（n ^ 2）
        # 空间复杂度： O (n ^ 2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j] 代表从第i个字符到第j个字符是否是回文子串
        res = ""
        for col in range(n):
            for row in range(col + 1):
                if s[row] == s[col] and (col - row < 2 or dp[row + 1][col - 1]):
                    dp[row][col] = True
                    if len(res) < col - row + 1:
                        res = s[row:col + 1]
        # print(dp)
        return res
