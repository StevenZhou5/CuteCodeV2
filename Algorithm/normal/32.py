# 32. 最长有效括号
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：
#
# 输入：s = ""
# 输出：0
#
#
# 提示：
#
# 0 <= s.length <= 3 * 104
# s[i] 为 '(' 或 ')'

class Solution():

    def get_longest_with_counter(self, str):
        # 注意，为了避免(() 左括号始终多余右括号的情况，我们要从后向前遍历
        if not str:
            return 0
        left_cnt = 0
        right_cnt = 0

        res = 0
        for i in range(len(str) - 1, -1, -1):
            if str[i] == ")":  # 如果是右边括号，只需要计数
                right_cnt += 1
                continue
            left_cnt += 1

            if left_cnt > right_cnt:  # 左括号多说明已经不合法，重置
                left_cnt, right_cnt = 0, 0
            else:  # 此时left_cnt <= right_cnt, 合法长度为left的两倍
                cur_len = left_cnt << 1
                res = max(res, cur_len)

        return res

    def get_longest_with_stack(self, str):
        if not str:
            return 0

        stack = [-1]
        res = 0
        cur_len = 0
        for i in range(len(str)):
            # 遇到 "(" 直接把当前左括号的索引放入栈中
            if str[i] == "(":
                stack.append(i)
                continue
            # 遇到 ")" 时
            # 如果栈顶为"("取出一个"("当前有效长度+2，
            if stack[-1] != -1:
                cur_len += 2
                res = max(res, cur_len)
                stack.pop()
            else:  # 如果栈顶没有"(",说明截止到此时，字符串已经不是合法括号了，重置长度
                cur_len = 0
        return res

    def get_longest_with_dp(self, str):
        if not str:
            return 0
        # 状态定义：dp[i] 以str[i]为结尾的最长有效括号的长度，如果str[i]为"("始终为0，如果为")"有两种情况：和前一个匹配，和前i-dp[i-1]的前一个匹配或者不匹配
        dp = [0] * len(str)
        dp[0] = 0

        for i in range(1, len(str)):
            # print(str[i])
            if str[i] == "(":
                dp[i] = 0
                continue
            # i 为 ")"时的情况
            if str[i - 1] == "(":
                dp[i] = (dp[i - 2] if i > 1 else 0) + 2
                continue
            # i - 1 为 "）"时
            last_left_idx = i - dp[i - 1] - 1
            if last_left_idx >= 0 and str[last_left_idx] == "(":
                # last_left_idx 前可能还有连续有效的括号，所以要加上dp[last_left_idx - 1]
                dp[i] = (dp[last_left_idx - 1] if last_left_idx > 0 else 0) + dp[i - 1] + 2

        return (dp, max(dp))


strs = ["()", "(()())", "((()))", "(()(())", "()(())))", "(((", ")))"]
solu = Solution()
for str in strs:
    print("cur_str:", str, "; get_longest_with_counter:", solu.get_longest_with_counter(str), "; get_longest_with_dp:",
          solu.get_longest_with_dp(str), "get_longest_with_stack:", solu.get_longest_with_stack(str))

# print(solu.get_longest_with_dp("()"))
