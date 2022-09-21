# 85. 最大矩形
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 示例 2：
#
# 输入：matrix = []
# 输出：0
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
# 示例 4：
#
# 输入：matrix = [["1"]]
# 输出：1
# 示例 5：
#
# 输入：matrix = [["0","0"]]
# 输出：0
#
#
# 提示：
#
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 动态规划
        # 时间复杂度：O(m^2 * n)
        # 空间复杂度：O(m * n )
        # 状态的定义
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # dp[i][j] 代表第i,j 位置左边有多少个连续的1，包括i，j位置

        res = 0
        for i in range(m):
            for j in range(n):
                cur_valid = int(matrix[i][j])
                if not cur_valid:
                    continue
                dp[i][j] = cur_valid + (dp[i][j - 1] if j > 0 else 0)
                w = dp[i][j]
                h = 1
                cur_max = w * h
                for k in range(i - 1, -1, -1):
                    if not dp[k][j]:
                        break
                    w = min(w, dp[k][j])
                    h += 1
                    cur_max = max(cur_max, w * h)
                res = max(res, cur_max)

                # print(dp)
        return res
