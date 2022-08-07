# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
# 提示：
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
# 进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # 两层循环 ： O(n^2) 的时间复杂度
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # 使用map：O(n) 的时间复杂度,循环两次
        # n = len(nums)
        # num_idx_map = {}
        # for idx in range(n):
        #     num_idx_map[nums[idx]] = idx

        # for i in range(n-1):
        #     another_num = target - nums[i]
        #     if another_num in num_idx_map and num_idx_map[another_num] != i:
        #         return [i,num_idx_map[another_num]]

        # 使用map且循环一次
        n = len(nums)
        num_idx_map = {}
        for idx in range(n):
            another_num = target - nums[idx]
            if another_num in num_idx_map:
                return [num_idx_map[another_num], idx]
            num_idx_map[nums[idx]] = idx


solu = Solution()
print(solu.twoSum([2, 7, 11, 15], 9))
