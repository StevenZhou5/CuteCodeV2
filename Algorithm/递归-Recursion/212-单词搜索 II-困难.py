# 212. 单词搜索 II
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
# 提示：
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:

        # 递归 + 回溯 + 字典树：时间复杂度O(m×n×3^l)；空间复杂度O(k * l); k为单词的个数，l为单词的长度；
        self.trie_root = {}
        self.end_label = "#"
        for word in words:
            cur_node = self.trie_root
            for c in word:
                cur_node = cur_node.setdefault(c, {})
            cur_node[self.end_label] = True
        # print(self.trie_root)

        self.m, self.n = len(board), len(board[0])
        self.visted_matrix = [[False] * self.n for _ in range(self.m)]
        self.move_actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.res = set()

        def recursion(row, col, cur_node, cur_str):
            # print(row, col,board[row][col], cur_node, cur_str)
            if board[row][col] not in cur_node:
                # print(board[row][col], cur_node)
                return
            next_str = cur_str + board[row][col]  # 注意，这个一定要
            if cur_node[board[row][col]].get(self.end_label, False):
                self.res.add(next_str)

            self.visted_matrix[row][col] = True
            for d_row, d_col in self.move_actions:
                next_row, next_col = row + d_row, col + d_col
                if next_row < 0 or next_row > self.m - 1 or next_col < 0 or next_col > self.n - 1 or \
                        self.visted_matrix[next_row][next_col]:
                    continue
                recursion(next_row, next_col, cur_node[board[row][col]], next_str)
            self.visted_matrix[row][col] = False

            # 如果找不到，我们可以进行剪枝，把当前

        for i in range(self.m):
            for j in range(self.n):
                recursion(i, j, self.trie_root, '')
        # recursion(0, 0, self.trie_root, '')
        return list(self.res)
