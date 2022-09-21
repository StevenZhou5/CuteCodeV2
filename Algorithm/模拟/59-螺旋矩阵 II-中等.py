# 59. 螺旋矩阵 II
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 示例 2：
#
# 输入：n = 1
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= n <= 20
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # 模拟 + 逐层遍历
        # 时间复杂度： O（n ^ 2）
        # 空间复杂度： O（1）
        res = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        cur_val = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res[top][col] = cur_val
                cur_val += 1
            for row in range(top + 1, bottom + 1):
                res[row][right] = cur_val
                cur_val += 1
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    res[bottom][col] = cur_val
                    cur_val += 1
                for row in range(bottom - 1, top, -1):
                    res[row][left] = cur_val
                    cur_val += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res
