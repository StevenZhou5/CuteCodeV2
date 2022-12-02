# 764. 最大加号标志
# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0
#
# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
#
# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。
#
#
#
# 示例 1：
#
#
#
# 输入: n = 5, mines = [[4, 2]]
# 输出: 2
# 解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
# 示例 2：
#
#
#
# 输入: n = 1, mines = [[0, 0]]
# 输出: 0
# 解释: 没有加号标志，返回 0 。
#
#
# 提示：
#
# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# 每一对 (xi, yi) 都 不重复​​​​​​​
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 动态规划
        # 时间复杂度 O (n ^ 2)
        # 空间复杂度 O (n ^ 2)
        # 状态定义：dp[row][col] 存储上下左右连续1的个数
        dp_matrix = [[[1] * 4 for j in range(n)] for i in range(n)]
        for x, y in mines:
            for i in range(4):
                dp_matrix[x][y][i] = 0

        for i in range(n):
            for j in range(n):
                if dp_matrix[i][j][0] == 0:
                    continue
                # step2： 状态转移
                if j > 0:  # 上
                    dp_matrix[i][j][0] = dp_matrix[i][j - 1][0] + 1
                if i > 0:  # 左
                    dp_matrix[i][j][1] = dp_matrix[i - 1][j][1] + 1

        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp_matrix[i][j][0] == 0:
                    continue
                # step2: 状态转移
                if j < n - 1:  # 右
                    dp_matrix[i][j][2] = dp_matrix[i][j + 1][2] + 1
                if i < n - 1:  # 下
                    dp_matrix[i][j][3] = dp_matrix[i + 1][j][3] + 1

                res = max(res, min(dp_matrix[i][j]))  # 此时可以计算最大十字了

        return res
