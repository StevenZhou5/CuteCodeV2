# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
# 示例 3：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
#
#
# 提示：
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        # 递归 + 回溯 + 二进制状态压缩: 时间复杂度O(m * n * 3^len(word))， 空间复杂度O(m) - 使用二进制状态压缩，O(m * n)不使用二进制状态压缩
        self.m, self.n = len(board), len(board[0]),  # 空间复杂度O(m * n)
        # self.visted_matrix = [[False] * self.n  for _ in range(self.m)] # 直接用数组记录可以，
        self.visted_matrix = [0] * self.m  # 因为n <= 6 所以可以使用二进制状态压缩，
        self.move_actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def recursion(row, col, word_idx):
            # print(row, col,cur_word, self.visted_matrix[row][col], board[row][col])
            if board[row][col] != word[word_idx]:
                return False
            if word_idx == len(word) - 1:  # 如果已经是最后一个字符，而且匹配成功了，返回True
                return True

            self.visted_matrix[row] |= 1 << col  # 记录已经被访问了
            for d_row, d_col in self.move_actions:
                next_row, next_col = row + d_row, col + d_col
                if next_row < 0 or next_row > self.m - 1 or next_col < 0 or next_col > self.n - 1 or (
                        self.visted_matrix[next_row] >> next_col) & 1:
                    continue
                if recursion(next_row, next_col, word_idx + 1):
                    return True  # 只要有一个方向OK， return True
            self.visted_matrix[row] ^= 1 << col  # 回溯
            return False  # 四个方向都不行，returnFalse

        for i in range(self.m):
            for j in range(self.n):
                if recursion(i, j, 0):
                    return True
        return False
