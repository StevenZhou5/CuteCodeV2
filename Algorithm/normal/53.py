# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
# 示例 4：
#
# 输入：nums = [-1]
# 输出：-1
# 示例 5：
#
# 输入：nums = [-100000]
# 输出：-100000
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#  
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return None

        res = nums[0]
        cur = nums[0]  # 选中当前位置的值可以得到的最大加和
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            res = max(cur, res)
        return res


solu = Solution()
from random import randint

nums = [randint(-10, 10) for _ in range(randint(0, 10))]
print(nums)
print("res:", solu.maxSubArray(nums))
