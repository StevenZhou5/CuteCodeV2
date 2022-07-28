# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
# 提示：
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution():
    def get_rain(self, height):
        n = len(height)
        left_to_right = [height[0]]
        for i in range(1, n):
            left_to_right.append(height[i] if height[i] > left_to_right[-1] else left_to_right[-1])

        right_to_left = [height[-1]]
        for i in range(n - 2, -1, -1):
            right_to_left.append(height[i] if height[i] > right_to_left[-1] else right_to_left[-1])

        right_to_left.reverse()

        print(left_to_right, right_to_left)
        res = 0
        for i in range(n):
            res += min(left_to_right[i], right_to_left[i]) - height[i]

        return res


solu = Solution()
height = [4, 2, 0, 3, 2, 5]
print("res:", solu.get_rain(height))
