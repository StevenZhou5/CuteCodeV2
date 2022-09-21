# 312. 戳气球
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
# 求所能获得硬币的最大数量。
#
#
#
# 示例 1：
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 示例 2：
#
# 输入：nums = [1,5]
# 输出：10
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

class Solution:
    def maxCoins(self, nums: [int]) -> int:
        # 核心思路是 逆向思维，考虑如何添加，而不要考虑如何减少

        # 递归 + 记忆化搜索
        # 时间复杂度：O (n ^ 3), 3层循环，每层O(n)
        # 空间复杂度：O(n ^ 2)
        # nums = [1] + nums + [1] # 在头尾部添加哨兵
        # n = len(nums)
        # # solve_map = {}
        # @lru_cache(None)
        # def solve(i, j): # 左开右开， 找到在(i, j) 区间的能获得的最大值
        #     if i >= j - 1: # 当i，j相邻或者i > j 时都没有位置可插入
        #         return 0
        #     # if (i, j) in solve_map:
        #     #     return solve_map[(i, j)]
        #     res = 0
        #     for mid in range(i + 1, j):
        #         res = max(res, nums[i] * nums[mid] * nums[j] + solve(i, mid) + solve(mid, j))
        #     # solve_map[(i,j)] = res
        #     return res
        # return solve(0, n - 1)

        # 动态规划
        # 时间复杂度：O (n ^ 3), 3层循环，每层O(n)
        # 空间复杂度：O(n ^ 2)
        # step1 状态定义
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # dp[i, j] 代表在(i, j) 左开右开区间能获得的最大值
        # print(nums)
        # print(dp)
        for i in range(2, n):  # 斜线从对角线开始，依次向右上角毕竟
            row, col = 0, i
            while row < n - i and col < n:
                # 状态转义
                for mid in range(row + 1, col):
                    dp[row][col] = max(dp[row][col], nums[row] * nums[mid] * nums[col] + dp[row][mid] + dp[mid][col])
                row += 1
                col += 1
        # print(dp)
        return dp[0][-1]
