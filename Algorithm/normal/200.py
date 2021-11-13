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
class Solution():
    def get_land_cnt_with_dfs(self, grid):
        if not grid:
            return 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        move_actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上，下，左，右

        def dfs(cur_row, cur_col):
            if cur_row < 0 or cur_row > row_cnt - 1 or cur_col < 0 or cur_col > col_cnt - 1 or grid[cur_row][
                cur_col] == "0":
                return
            grid[cur_row][cur_col] = "0"
            for row_act, col_act in move_actions:
                dfs(cur_row + row_act, cur_col + col_act)

        res = 0
        for row in range(row_cnt):
            for col in range(col_cnt):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
                    # print(grid)
        return res

    def get_land_cnt_with_union_find_sets(self, grid):
        if not grid:
            return 0
        row_cnt = len(grid)
        col_cnt = len(grid[0])

        class union_find_set():
            def __init__(self, parent=None, rank=1):
                self.parent = parent
                self.rank = rank

            def get_root(self):
                cur_root = self
                while cur_root.parent:
                    cur_root = cur_root.parent
                return cur_root

        def merge_two_union_find_set(a, b):
            if not a and not b:
                return None
            if not a:
                return b.get_root()
            if not b:
                return a.get_root()
            root_a = a.get_root()
            root_b = b.get_root()
            if root_a == root_b:
                return root_a
            if root_a.rank == root_b.rank:
                root_a.rank += 1
                root_b.parent = root_a
                return root_a
            if root_a.rank > root_b.rank:
                root_b.parent = root_a
                return root_a
            root_a.parent = root_b
            return root_b

        root_set = set()
        for row in range(row_cnt):
            for col in range(col_cnt):
                if grid[row][col] == "1":
                    # print("row:%d;col:%d;" % (row, col))
                    root_up = grid[row - 1][col] if row > 0 and grid[row - 1][col] != "0" else None
                    root_left = grid[row][col - 1] if col > 0 and grid[row][col - 1] != "0" else None
                    # print("root_set_len:", len(root_set), "; root_up:", root_up, "；root_left:", root_left)
                    merge_root = merge_two_union_find_set(root_up, root_left)
                    grid[row][col] = merge_root if merge_root else union_find_set()
                    if root_up in root_set:
                        root_set.remove(root_up)
                    if root_left in root_set:
                        root_set.remove(root_left)
                    root_set.add(grid[row][col])
        return len(root_set)


solu = Solution()
grid = [
    ["1", "1", "1", "0", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "1", "1"]
]
print("grid:", grid)
# print("res:", solu.get_land_cnt_with_dfs(grid))
print("res_merge_two_union_find_set:", solu.get_land_cnt_with_union_find_sets(grid))
