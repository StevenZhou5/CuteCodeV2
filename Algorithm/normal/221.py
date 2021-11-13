# 221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [
# ["1","0","1","0","0"],
# ["1","0","1","1","1"],
# ["1","1","1","1","1"],
# ["1","0","0","1","0"]
# ]
# 输出：4
# 示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'

class Solution():

    def max_square(self, matrix):
        if not matrix:
            return 0
        max_len = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0
                    continue
                up_len = matrix[row - 1][col] if row > 0 else 0
                left_len = matrix[row][col - 1] if col > 0 else 0
                left_up_len = matrix[row - 1][col - 1] if row > 0 and col > 0 else 0
                cur_len = min(up_len, left_len, left_up_len) + 1
                matrix[row][col] = cur_len
                max_len = max(max_len, cur_len)

        return max_len ** 2


solu = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "0", "1"],
    ["1", "0", "0", "1", "1"]
]
print("res:", solu.max_square(matrix))
