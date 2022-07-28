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
# s 只含小写英文字母。
# p 只含小写英文字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符

class Solution():
    def is_match(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        def is_match(chr1, chr2):
            return chr2 == '.' or chr1 == chr2

        for i in range(0, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":  # 要么匹配0个，要么匹配k个
                    dp[i][j] |= dp[i][j - 2]
                    if p[j - 2] == s[i - 1]:  # 如果s当前字符和p的"*"前面的字符一致
                        dp[i][j] |= dp[i][j - 1]  # 值匹配当前这一个字符
                        dp[i][j] |= dp[i - 1][j]  # s的前一个字符和"*"一样，匹配多个
                else:
                    if is_match(s[i - 1], p[j - 1]):
                        dp[i][j] |= dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        print(dp)
        return dp[-1][-1]


solu = Solution()
print("res:", solu.is_match("sssddddddlcaa", "s*d.d*.cd*a*"))
