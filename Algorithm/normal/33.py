# 33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
# 提示：
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？


class Solution:

    def search1(self, nums, target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_first(self, nums, target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] >= target:
                if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_last(self, nums, target):
        if not nums:
            return
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] <= target:
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                    return mid
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_latest_small(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] >= target:
                if nums[mid] >= target and (mid == 0 or nums[mid - 1] < target):
                    return -1 if mid == 0 else (mid - 1)
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_latest_large(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] <= target:
                if nums[mid] <= target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                    return -1 if (mid == len(nums) - 1) else (mid + 1)
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_trans(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[right]:  # 完全有序
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] == target:  # 如果左边的值等于目标值，则直接返回
                    return left
                if target > nums[left]:  # 如果target 大于最左边值，从左半边搜索
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


from random import randint

nums = [randint(-5, 5) for _ in range(10)]
nums.sort()
target_num = randint(-10, 10)
print("nums:", nums, "; target_num:", target_num)
solu = Solution()
print("res:", solu.search1(nums, target_num))
print("res_first:", solu.search_first(nums, target_num))
print("res_last:", solu.search_last(nums, target_num))
print("res_latest_small:", solu.search_latest_small(nums, target_num))
print("res_latest_large:", solu.search_latest_large(nums, target_num))

trans_idx = randint(0, len(nums))
trans_nums = nums[trans_idx:] + nums[0:trans_idx]
print("trans nums:", trans_nums)
print("res_search_trans:", solu.search_trans(trans_nums, target_num))
