# 912. 排序数组
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
import heapq


class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        # 堆排：
        if not nums:
            return []
        heapq.heapify(nums)  # 构造小顶堆
        return [heapq.heappop(nums) for _ in range(len(nums))]  # 每次取出堆顶元素，并重新调整堆位小顶堆
        return res
