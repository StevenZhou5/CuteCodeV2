# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100

class Solution():
    def min_path(self, grid):
        if not grid:
            return 0
        print("origin grid:", grid)
        # 状态定义：到当前位置所需的最小路径,直接使用grid就行，不需要额外空间
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:  # 0，0位置不需要判断
                    continue
                up = grid[row - 1][col] if row > 0 else float('inf')
                left = grid[row][col - 1] if col > 0 else float('inf')
                grid[row][col] = min(up, left) + grid[row][col]

        print("final grid:", grid)
        return grid[-1][-1]


solu = Solution()
grid = [
    [1, 3, 1],
    [1, 5, 5],
    [4, 2, 1]
]
solu.min_path(grid)
