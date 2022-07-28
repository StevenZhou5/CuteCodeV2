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
    def get_longest_palindrome_str_with_dp(self, s):
        n = len(s)
        # 状态定义：dp[i][j] 字符串的第i个位置到第j个位置形成的子串是否是回文子串
        # j 必须大于i ， 矩阵对角线的初始值为True
        dp = [[True if col == row else False for col in range(n)] for row in range(n)]
        print(dp)
        # 状态转移：
        # 当j-i>1是 dp[i][j] = True  if dp[i+1][j-1] and s[i] == s[j] else False ;
        # 当j-i==1时 dp[i][j] = True if s[i] == s[j] else False
        res = s[0]
        for col in range(1, n):  # 列从左到右
            for row in range(col - 1, -1, -1):  # 行从下到上，当然要保证row < col
                if col - row == 1:
                    dp[row][col] = s[row] == s[col]
                else:
                    dp[row][col] = True if dp[row + 1][col - 1] and s[row] == s[col] else False

                if dp[row][col] and (col - row + 1) > len(res):
                    res = s[row:col + 1]
        print(dp)
        return res

    def get_longest_palindrome_str_with_dp_v2(self, s):
        n = len(s)
        # 节省空间复杂度，只用一列
        dp = [False] * n
        res = ""
        for col in range(n):
            print(dp)
            for row in range(col + 1):  # 因为要一栏dp[row+1][col-1] 所以要让row从小到大更新，这样就能保证用的状态是上一列的
                if col - row > 1:
                    dp[row] = True if dp[row + 1] and s[row] == s[col] else False
                elif col - row == 1:
                    dp[row] = True if s[row] == s[col] else False
                else:  # row == col
                    dp[row] = True

                if dp[row] and (col - row + 1) > len(res):
                    res = s[row:col + 1]

        return res


solu = Solution()
s = "babad"
# print("res:", solu.get_longest_palindrome_str_with_dp(s))
print("res:", solu.get_longest_palindrome_str_with_dp_v2(s))
