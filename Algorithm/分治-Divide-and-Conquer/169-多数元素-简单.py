# 169. 多数元素
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
# 提示：
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法： 本质上是分治
        candidate = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:  # 当count == 0 的时候，说明这一段中出现最多的数和其他数的数目一样，此时这段的分治结束，开始下一段的分治
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

        # map计数：时间复杂度O(n); 空间复杂度O(n)
        # min_count = len(nums) >> 1
        # num_counter = {}
        # for num in nums:
        #     num_counter[num] = num_counter.get(num, 0) + 1
        #     if num_counter[num] > min_count:
        #         return num
