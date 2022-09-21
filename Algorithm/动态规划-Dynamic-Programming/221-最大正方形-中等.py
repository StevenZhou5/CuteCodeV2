# 221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
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

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划 :
        # step 1 状态定义 matrix[i][j] 代表以第i行第j列为末尾元素，当前行有多少个连续的1
        # m, n = len(matrix), len(matrix[0])
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == "0":
        #             matrix[i][j] = 0
        #             continue
        #         # 状态转义
        #         matrix[i][j] = 1 + (matrix[i][j - 1] if j > 0 else 0 )
        #         h = 0
        #         w = matrix[i][j]
        #         for k in range(i, -1 , -1):
        #             h += 1
        #             w = min(w, matrix[k][j])
        #             if w < h:
        #                 break
        #             res = max(h * h, res)
        # # print(matrix)
        # return res

        # 动态规划 + 单调栈
        # m, n = len(matrix), len(matrix[0])
        # res = 0
        # for i in range(m):
        #     stack = [] # 单调递增栈
        #     for j in range(n):
        #         if matrix[i][j] == "0":
        #             matrix[i][j] = 0
        #             # stack.clear()
        #             # continue
        #         else:
        #             matrix[i][j] = 1 + (matrix[i - 1][j] if i > 0 else 0)
        #         while stack and matrix[i][j] < matrix[i][stack[-1]]:
        #             move_j = stack.pop()
        #             side_len = min(j - (stack[-1] if stack else -1) - 1 , matrix[i][move_j])
        #             res = max(side_len * side_len, res)
        #         stack.append(j)
        #     while stack:
        #         move_j = stack.pop()
        #         side_len = min(n - (stack[-1] if stack else -1) - 1, matrix[i][move_j])
        #         res = max(side_len * side_len, res)
        # # print(matrix)
        # return res

        # 简单动态规划
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    continue
                matrix[i][j] = 1
                if i > 0 and j > 0:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                res = max(res, matrix[i][j] ** 2)
        return res
