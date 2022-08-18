# 37. 解数独
# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
#
#
# 示例 1：
#
#
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#
#
#
#
# 提示：
#
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解

class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 剪枝 + 递归 + 回溯 + 状态压缩 + 位远算：时间复杂度取决去要填写的空格中需要尝试的数字，
        self.row_states = [0] * 9
        self.col_states = [0] * 9
        self.matrix_states = [0] * 9
        # 初始化状态，进行剪枝
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                cur_num = int(board[row][col])
                cur_state = 1 << cur_num
                matrix_idx = (row // 3) * 3 + col // 3
                self.row_states[row] |= cur_state
                self.col_states[col] |= cur_state
                self.matrix_states[matrix_idx] |= cur_state

        # print(self.row_states, self.col_states, self.matrix_states)

        self.all_states = (1 << 10) - 1 - 1  # 这里多减去一个1 是因为数字1-9 用的是二进制的第1到第9位，0位置没有用

        def recursion(row, col):
            if row >= 9 or col >= 9:  # 找到了一组解
                return True
            if board[row][col] != ".":
                if col < 8:
                    return recursion(row, col + 1)
                else:
                    return recursion(row + 1, 0)

            matrix_idx = (row // 3) * 3 + col // 3
            valid_num_states = self.all_states & (
                ~(self.row_states[row] | self.col_states[col] | self.matrix_states[matrix_idx]))  # 得到剪枝后的所有可填写的值
            while valid_num_states:
                valid_state = valid_num_states & (-valid_num_states)  # 取出最后一位1
                valid_num = bin(valid_state - 1).count('1')
                # print(valid_num)
                valid_num_states = valid_num_states & (valid_num_states - 1)  # 去掉最后一位1

                # 写入值，更新状态
                board[row][col] = str(valid_num)
                self.row_states[row] |= valid_state
                self.col_states[col] |= valid_state
                self.matrix_states[matrix_idx] |= valid_state

                # 递归
                other_valid = False
                if col < 8:
                    other_valid = recursion(row, col + 1)
                else:
                    other_valid = recursion(row + 1, 0)

                if other_valid:
                    return True

                # 回溯，尝试下一个值
                board[row][col] = "."
                self.row_states[row] ^= valid_state  # 把对应二进制位置为0
                self.col_states[col] ^= valid_state
                self.matrix_states[matrix_idx] ^= valid_state

            return False

        recursion(0, 0)
