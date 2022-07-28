# 剑指 Offer 42. 连续子数组的最大和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 提示：
#
# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100
class Solution():

    def get_max_sub_val(self, nums):
        n = len(nums)
        dp_pre = nums[0]
        res = dp_pre

        for i in range(1, n):
            dp_pre = max(nums[i], dp_pre + nums[i])
            res = max(res, dp_pre)

        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solu = Solution()
print("res:", solu.get_max_sub_val(nums))
