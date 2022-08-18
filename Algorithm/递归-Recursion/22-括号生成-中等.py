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

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归: 时间复杂度O(4^n / n ^ 0.5), 空间复杂度O(n)
        res = []

        def recursion(cur_str, left_used, right_used, n):
            if left_used == right_used == n:
                res.append(cur_str)
                return

            if left_used < n:
                recursion(cur_str + '(', left_used + 1, right_used, n)

            if right_used < left_used:  # 不需要额外判断right_used < n , 因为left_used 不会大于n
                recursion(cur_str + ')', left_used, right_used + 1, n)

        recursion('', 0, 0, n)
        return res
