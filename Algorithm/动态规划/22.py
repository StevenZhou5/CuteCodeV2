# 22. 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
# 提示：
#
# 1 <= n <= 8

class Solution():

    def get_all_res_with_dp(self, n):
        res = []

        # 状态定义：dp[left_used][right_used] 可以从
        # dp[left_used-1][right_used] 和 dp[left_used][right_used-1]转移过来

        def recursion(cur_str, left_used, right_used):
            if left_used == right_used == n:
                res.append(cur_str)

            # 递归的状态转义
            if left_used < n:
                recursion(cur_str + "(", left_used + 1, right_used)

            if right_used < left_used:
                recursion(cur_str + ")", left_used, right_used + 1)

        recursion("", 0, 0)
        return res


solu = Solution()
n = 3
print("res:", solu.get_all_res_with_dp(n))
