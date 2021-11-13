# 85. 最大矩形
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [
# ["1","0","1","0","0"],
# ["1","0","1","1","1"],
# ["1","1","1","1","1"],
# ["1","0","0","1","0"]
# ]
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
# 0 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
class Solution():
    def get_max_rectangle(self, matrix):
        if not matrix:
            return 0
        # 状态，存储[lenth] 以当前点为最右边的点，在当前行的最长连续长度
        res = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0
                    continue
                matrix[row][col] = 1 + (matrix[row][col - 1] if col > 0 else 0)
                width = matrix[row][col]  # 初始矩形的最短宽度为
                height = 1
                cur_max_rectangle_area = width * height
                for i in range(1, row + 1):
                    if matrix[row][col - i] == 0:
                        break
                    width = min(width, matrix[row - i][col])
                    height += 1
                    cur_max_rectangle_area = max(cur_max_rectangle_area, width * height)
                res = max(res, cur_max_rectangle_area)
        print(matrix)
        return res


solu = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "1", "0", "1", "1"],
    ["1", "1", "0", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print("res:", solu.get_max_rectangle(matrix))
