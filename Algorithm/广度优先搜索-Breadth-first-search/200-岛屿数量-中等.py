# 200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
# 输入：grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：
#
# 输入：grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# 输出：3
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'

# 并查集
# class UnionFind:
#     def __init__(self, grid):
#         m, n = len(grid), len(grid[0])
#         self.root = [0] * (m * n)
#         self.rank = [0] * (m * n)
#         self.count = 0  # 用来记录‘1’ 所有不同root的数量
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '0':
#                     continue
#                 idx = i * n + j
#                 self.root[idx] = idx
#                 self.rank[idx] = 1
#                 self.count += 1
#
#     def find_root(self, i):
#         if self.root[i] != i:
#             self.root[i] = self.find_root(self.root[i])
#         return self.root[i]
#
#     def union(self, x, y):
#         x_root = self.find_root(x)
#         y_root = self.find_root(y)
#         if x_root == y_root:
#             return
#
#         if self.rank[x_root] < self.rank[y_root]:
#             x_root, y_root = y_root, x_root
#         self.root[y_root] = x_root  # 上面的判断保证了y_root的rank <= x_root 的rank
#         if self.rank[x_root] == self.rank[y_root]:
#             self.rank[x_root] += 1
#         self.count -= 1
#
#     def get_count(self):
#         return self.count


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        # 染色 + BFS: 时间复杂度O(m * n), 每个结点只操作一次 ; 空间复杂度O(min(m,n))；
        from collections import deque
        m, n = len(grid), len(grid[0])
        res = 0
        move_actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = '0'  # 一定要在添加的时候就染色
                    while queue:
                        cur_row, cur_col = queue.popleft()
                        for d_row, d_col in move_actions:
                            new_row = cur_row + d_row
                            new_col = cur_col + d_col
                            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1':
                                queue.append((new_row, new_col))
                                grid[new_row][new_col] = '0'
        # print(grid)
        return res

        # 并查集：
        # 时间复杂度：O(MN \times \alpha(MN))O(MN×α(MN))，
        # 其中 MM 和 NN 分别为行数和列数。注意当使用路径压缩（见 find 函数）和按秩合并（见数组 rank）实现并查集时，
        # 单次操作的时间复杂度为 \alpha(MN)α(MN)，其中 \alpha(x)α(x) 为反阿克曼函数，当自变量 xx 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 \alpha(x)α(x) 的值不会超过 55，
        # 因此也可以看成是常数时间复杂度。
        # 空间复杂度：O(MN)O(MN)，这是并查集需要使用的空间。
        # union_find = UnionFind(grid)
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '0':
        #             continue
        #         # 和上面合并
        #         if i > 0 and grid[i - 1][j] == '1':
        #             union_find.union(i * n + j, (i - 1) * n + j)
        #
        #         # 和左边合并
        #         if j > 0 and grid[i][j - 1] == '1':
        #             union_find.union(i * n + j, i * n + j - 1)
        # return union_find.get_count()
