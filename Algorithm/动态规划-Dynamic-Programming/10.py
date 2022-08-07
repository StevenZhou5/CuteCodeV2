# 10. 正则表达式匹配
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#
# 示例 1：
#
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3：
# 
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4：
#
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5：
#
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false
#
#
# 提示：
#
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符

class Solution():
    def is_match(self, s, p):
        # 状态定义 dp[i][j] 代表s的前i个字符与p的前j个字符是否匹配
        # 状态转移：
        # 如果p[j] 不为 * , 那么 s[i] 必须match p[j] 即为 s[i] == p[j] 或者 p[j] == . 则dp[i][j] = dp[i-1][j-1]; 否则dp[i][j] = False
        # 如果p[j] 为 *， 那么如果s[i] 与p[j-1]匹配：dp[i][j] = dp[i-1][j] or dp[i][j-2] ;否侧 dp[i][j] = dp[i][j-2]
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # 注意dp[0][0] 代表s的前0个字符即为"" 与 p 的前0个字符""匹配

        # dp[0][0] = True

        def match(chr1, chr2):
            # print(chr1, chr2)
            return chr1 == chr2 or chr2 == '.'

        for row in range(m + 1):
            for col in range(n + 1):
                if row == col == 0:
                    dp[row][col] = True  # 空字符串 和 空字符串是匹配的
                    continue
                # 一定要用 s[start_idx:start_idx+1] 的方式来取对应位置的字符，不然python的s[-1] 会取到最后一个字符
                if p[col - 1:col] != "*":
                    if match(s[row - 1:row], p[col - 1:col]):
                        dp[row][col] = dp[row - 1][col - 1]
                    else:
                        dp[row][col] = False
                else:
                    if match(s[row - 1:row], p[col - 2:col - 1]):
                        dp[row][col] = dp[row - 1][col] or dp[row][col - 2]
                    else:
                        dp[row][col] = dp[row][col - 2]
        print(dp)
        return dp[m][n]


solu = Solution()
s = "aab"
p = "c*a*b"
print("res:", solu.is_match(s, p))
