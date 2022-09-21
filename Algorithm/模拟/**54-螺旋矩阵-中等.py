# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 模拟 + 记忆化
        # 时间复杂度 O(m * n)
        # 空间复杂度 O(m * n) 记录每个位置是否被访问
        # move_actions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 右、下、左、上
        # m, n = len(matrix), len(matrix[0])
        # res = []
        # visted_set = set() # 也可以用矩阵
        # for i in range((m + 1) >> 1):
        #     row, col = i, i
        #     for d_r, d_c in move_actions:
        #         while  i <= row < m - i and  i <= col < n - i:
        #             if (row, col) not in visted_set:
        #                 visted_set.add((row, col))
        #                 res.append(matrix[row][col])
        #             row += d_r
        #             col += d_c

        #         row -= d_r
        #         col -= d_c

        # return res

        # 逐层访问
        # 时间复杂度： O(m * n)
        # 空间复杂度： O(1)
        res = []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1

        while left <= right and top <= bottom:  # 这里也要用边界去判断
            for col in range(left, right + 1):  # 开始位置包括左上角元素
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if right > left and bottom > top:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):  # 因为开始包含了左上角元素，最后就不需要再额外添加左上角元素了
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res
