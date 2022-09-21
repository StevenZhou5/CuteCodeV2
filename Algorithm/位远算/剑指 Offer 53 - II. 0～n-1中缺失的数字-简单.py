# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
#
#
#
# 示例 1:
#
# 输入: [0,1,3]
# 输出: 2
# 示例 2:
#
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
#
#
# 限制：
#
# 1 <= 数组长度 <= 10000
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 排序： 确实的那个数字的索引位置和自身相等，否则就是n；
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)

        # 位运算：时间复杂度O(n), 空间复杂度O(1)
        res = 0
        for i, num in enumerate(nums):
            res ^= i ^ num  # x ^ x = 0; x ^ 0 = x;  a ^ b ^ c = a ^ c ^ b = a ^ (b ^ c)
        return res ^ len(nums)
