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
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        # 动态规划
        # 时间复杂度：O(m * n)
        # 空间复杂度: O(1) 直接复用grid
        # step1 状态定义；直接用grid来当做dp，grid[i][j] 代表到当前位置的最小路径和
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                # step2: 状态转移
                grid[i][j] = min(grid[i - 1][j] if i > 0 else float('inf'), grid[i][j - 1] if j > 0 else float('inf')) + \
                             grid[i][j]
        return grid[-1][-1]
