# 581. 最短无序连续子数组
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
#
#
# 示例 1：
#
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 示例 2：
#
# 输入：nums = [1,2,3,4]
# 输出：0
# 示例 3：
#
# 输入：nums = [1]
# 输出：0
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
#
#
# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
#
class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        # 排序 + 比较
        # 时间复杂度：O(n * log n)
        # 空间复杂度：O(n)
        # sorted_nums = sorted(nums)
        # n = len(nums)
        # l = 0
        # for i in range(n):
        #     if nums[i] != sorted_nums[i]:
        #         l = i
        #         break
        # for j in range(n-1, -1, -1):
        #     if nums[j] != sorted_nums[j]:
        #         return j - l + 1
        # return 0

        # 双指针： 如果存在 0 <= l < r <= n-1; 其中l 到 r区间是我们要找的区间，那么区间内的所有数一定都比0到 l - 1中的数大，r + 1 到 n - 1 区间的数一定都比目标区间的数大；
        # 从左向右遍历，记录左边最大值，如果当前值比左边最大值小，说明他一定是l - r区间中的数，更新右边界，直到找到最后一个比左边最大值小的数即为r; 同理可以找到左边界；
        # 时间复杂度：O(n) 只用遍历一次
        # 空间复杂度：O(1)
        n = len(nums)
        r, max_val = -1, float('-inf')  # 为了找到右边界，需要把左边的最大值记录下来
        l, min_val = -1, float('inf')  # 为了找到左边界，需要把右边的最小值记录下来
        for i in range(n):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                r = i  # 当前值没有比左边的值都大，更新右边界

            j = n - i - 1
            if nums[j] <= min_val:
                min_val = nums[j]
            else:
                l = j  # 当前值没有比右边的数都小，更新左边界

        return 0 if r == -1 else (r - l + 1)
