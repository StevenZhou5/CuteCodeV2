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
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈 + 哨兵
        # 时间复杂度 O(n), 外层遍历添加一次，内层遍历弹出一次，总共2n次操作
        # 空间复杂度 O(n)，最多存储所有的高度到栈中
        heights.append(0)  # 在最后加入一个值为 0 的哨兵，这样就能保证一次遍历后，所有元素都一定出栈了；初始位置不用加0，因为可以在stack中存一个-1的索引位置当哨兵
        res = 0
        n = len(heights)
        stack = [-1]  # 存位置索引,初始存一个-1 的哨兵可以避免很多边界条件的判断
        for i in range(n):
            # print(i, stack, res)
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        # print(stack, res)
        # while len(stack) > 1:
        #     h = heights[stack.pop()]
        #     w = n - stack[-1] - 1
        #     res = max(res, w * h)

        return res
