# 52. N皇后 II
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
# 提示：
#
# 1 <= n <= 9

class Solution:
    def totalNQueens(self, n: int) -> int:
        # 递归 + 回溯 + 位运算: 时间复杂度 O (n!); 空间复杂度O(1)
        self.res = 0
        self.final_state = (1 << n) - 1

        # print(final_state)

        def recursion(col_state, left_state, right_state):
            # print(col_state, left_state, right_state)
            if col_state == self.final_state:
                self.res += 1
                return

            valid_col = self.final_state & (~(col_state | left_state | right_state))
            while valid_col:
                cur_col = valid_col & (-valid_col)
                valid_col = valid_col & (valid_col - 1)
                recursion(col_state | cur_col, (left_state | cur_col) << 1, (right_state | cur_col) >> 1)

        recursion(0, 0, 0)
        return self.res
