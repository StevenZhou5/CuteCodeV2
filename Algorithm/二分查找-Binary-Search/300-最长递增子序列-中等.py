# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
#
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
#
# 进阶：
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        # 动态规划： 时间复杂度O(n^2); 空间复杂度O(n)
        # n = len(nums)
        # # step1: 状态定义；
        # dp = [1] * n
        # res = 0
        # for i in range(n):
        #     for j in range(i - 1, -1, -1):
        #         if nums[j] < nums[i]:
        #             # step2：状态转移
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     res = max(res, dp[i])
        # return res

        # 贪心 + 二分查找：时间复杂度O(n * log n); 空间复杂度O(n)
        n = len(nums)
        lis = [nums[0]]
        for i in range(1, n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
                continue
            # 二分查找: 找到第一个比nums[i] 大或者相等的数替换掉
            l, r = 0, len(lis) - 1
            loc = r
            while l <= r:
                mid_idx = l + ((r - l) >> 1)
                if lis[mid_idx] >= nums[i]:  # 二分查找，找到第一个比target大或者相等的数(左边第一个和target相等的数)的
                    loc = mid_idx
                    r = mid_idx - 1
                else:
                    l = mid_idx + 1
            lis[loc] = nums[i]
        # print(lis)
        return len(lis)
