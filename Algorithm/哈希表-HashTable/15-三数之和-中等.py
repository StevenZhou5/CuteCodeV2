# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
#
# 输入：nums = []
# 输出：[]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[]
#
#
# 提示：
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # 使用Map实现 ： 时间复杂度O(n^2), 空间复杂度O(n)
        # if not nums:
        #     return []
        # nums.sort()
        # n = len(nums)
        # res = set()
        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     # num_map = {}  # 使用map比较直观
        #     num_set = set() # 也可以直接使用set
        #     for j in range(i+1, n):
        #         # if nums[j] in num_map:
        #             # res.add((num_map[nums[j]][0], num_map[nums[j]][1], nums[j]))
        #         # num_map[0-nums[i]-nums[j]] = [nums[i], nums[j]]

        #         if nums[j] in num_set: # 如果nums[j] 已经是第三个数了，那么就不需要再额外把第二个数(-(nums[i] + nums[j]))加到num_set中，因为加进去后面既使找到也是一组重复解
        #             res.add((nums[i],-(nums[i] + nums[j]) ,nums[j]))
        #         else:
        #             num_set.add(-(nums[i] + nums[j]))

        # return list(res)

        # 排序 + 双指针 : 时间复杂度O(N^2),空间复杂度O(1)
        if not nums:
            return []
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
