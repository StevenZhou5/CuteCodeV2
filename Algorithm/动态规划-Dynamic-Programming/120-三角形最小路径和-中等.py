# 120. 三角形最小路径和
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# 2
# 3 4
# 6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 示例 2：
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
# 提示：
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
#
#
# 进阶：
#
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？

class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        #  动态规划（从上向下）： 时间复杂度O(n^2): 两层循环； 空间复杂度O(n):虽然只存一行，但最后一行的数;
        # dp_pre = triangle[0]
        # for i in range(1,len(triangle)):
        #     # print(dp_pre)
        #     dp_cur = []
        #     for j in range(len(triangle[i])):
        #         dp_cur.append(min(dp_pre[j] if j < len(dp_pre) else float('inf'), dp_pre[j-1] if j > 0 else float('inf')) + triangle[i][j])
        #     dp_pre = dp_cur
        # # print(dp_pre)
        # return min(dp_pre)

        # 动态规划（从下向上）: 时间复杂度O(n ^ 2); 空间复杂度O(n);
        # dp_pre = triangle[-1]
        # for i in range(len(triangle) - 2, -1, -1):
        #     dp_cur = []
        #     for j in range(len(triangle[i])):
        #         dp_cur.append(min(dp_pre[j], dp_pre[j + 1]) + triangle[i][j])
        #     dp_pre = dp_cur
        # return dp_pre[0]  # 因为最顶上只有一个元素，所以不用再求min了

        # 动态规划（从下向上）+ 复用数组: 时间复杂度O(n ^ 2); 空间复杂度O(n);
        dp_min = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp_min[j] = min(dp_min[j], dp_min[j + 1]) + triangle[i][j]
            # dp_min.pop() # 如果要节省运行时内存，可以在每上一层的时候把最后一个元素移除掉，因为后面不会在用到
        return dp_min[0]
