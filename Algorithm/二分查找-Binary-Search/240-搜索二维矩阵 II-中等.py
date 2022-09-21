# 240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true
# 示例 2：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -109 <= target <= 109

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        # 时间复杂度： O(m * log n)
        # 空间复杂度： O(1)
        # m, n = len(matrix), len(matrix[0])
        # # 先找行，找右边界- 最后一个小于或等于target的值
        # # 左开右开，相邻终止
        # l, r = -1, m
        # while l + 1 < r:
        #     mid = (l + r) >> 1
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] > target:
        #         r = mid
        #     else:
        #         l = mid
        # if l == -1: # 所有值都比目标值大
        #     return False
        # # print(l) # 行的最大值
        # cl, cr = -1, n
        # while cl + 1 < cr:
        #     mid = (cl + cr) >> 1
        #     if matrix[0][mid] == target:
        #         return True
        #     elif matrix[0][mid] > target:
        #         cr = mid
        #     else:
        #         cl = mid
        # # print(cl) # 列的最大值
        # # 此时matrix[l][0]一定是第0列小于target的最大值
        # for i in range(l, -1 ,-1): # 逐行二分查找
        #     # 左开右开
        #     ll, lr = -1, cl + 1
        #     while ll + 1 < lr:
        #         mid = (ll + lr) >> 1
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             lr = mid
        #         else:
        #             ll = mid

        # return False

        # Z子型搜索
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(1)
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
