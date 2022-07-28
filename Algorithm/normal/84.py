# 84. 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
# 提示：
#
# 1 <= heights.length <=105
# 0 <= heights[i] <= 104

class Solution():

    def get_max_rectangle(self, heights):
        if not heights:
            return 0
        matrix_height = max(heights)
        matrix_width = len(heights)
        matrix = [[0] * matrix_width for _ in range(matrix_height)]

        # 初始化矩阵, matrix[i][j] 代表第i行以matrix[i][j]为最右点可以形成的长度
        for col in range(matrix_width):
            for i in range(heights[col]):
                row = matrix_height - i - 1
                matrix[row][col] = (matrix[row][col - 1] if col > 0 else 0) + 1
        print(matrix)

        res = 0
        for col in range(matrix_width):
            row = matrix_height - 1
            cur_rectangle_height = 0  # 当前高度
            cur_rectangle_width = matrix[row][col]
            while row >= 0 and matrix[row][col] > 0:
                cur_rectangle_height += 1
                cur_rectangle_width = min(cur_rectangle_width, matrix[row][col])
                res = max(res, cur_rectangle_width * cur_rectangle_height)

                row -= 1
        return res


solu = Solution()
heights = [2, 2, 5, 4, 2, 1]
[[0, 0, 0, 1, 0, 0],
 [0, 0, 1, 2, 0, 0],
 [0, 0, 1, 2, 0, 0],
 [0, 0, 1, 2, 0, 1],
 [1, 0, 1, 2, 3, 4],
 [1, 2, 3, 4, 5, 6]]
print("res:", solu.get_max_rectangle(heights))
