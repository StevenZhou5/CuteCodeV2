# 51. N 皇后
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
# 提示：
#
# 1 <= n <= 9
class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        # 递归 + 位运算（避开无效位）：时间复杂度 O(N!); 空间复杂度O(n) - 不算res；
        # res = []
        # cur_cols = [] # 建在外面可以节省空间复杂度
        # def recursion(col_used,left_used,right_used):
        #     if len(cur_cols) >= n:
        #         res.append(["." * col + "Q" + "." * (n-col-1) for col in cur_cols])
        #         return
        #     not_valid_col = col_used | left_used | right_used
        #     for i in range(n):
        #         if (not_valid_col >> i) & 1 == 0 : # 如果这个位置可用
        #             cur_col = 1 << i
        #             cur_cols.append(i)
        #             recursion(col_used | cur_col,(left_used | cur_col) << 1, (right_used | cur_col) >> 1)
        #             cur_cols.pop()

        # recursion(0,0,0)

        # return res

        # 递归 + 位运算（使用有效位）：时间复杂度 O(N!); 空间复杂度O(n) - 不算res；
        res = []
        cur_cols = []  # 建在外面可以节省空间复杂度

        def recursion(col_used, left_used, right_used):
            if len(cur_cols) >= n:
                res.append(["." * col + "Q" + "." * (n - col - 1) for col in cur_cols])
                return
            valid_col = ((1 << n) - 1) & ~(col_used | left_used | right_used)  # 得到有效位
            while valid_col:
                cur_col = valid_col & (-valid_col)  # 取到最后一位1
                valid_col = valid_col & (valid_col - 1)  # 去除valid_col最后一位1
                cur_cols.append(bin(cur_col - 1).count("1"))  # bin(position - 1).count("1") 是将二进制的列转换为数字列
                recursion(col_used | cur_col, (left_used | cur_col) << 1, (right_used | cur_col) >> 1)
                cur_cols.pop()

        recursion(0, 0, 0)

        return res
