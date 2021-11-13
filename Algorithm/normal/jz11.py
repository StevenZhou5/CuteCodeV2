# 剑指 Offer 11. 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
# 示例 1：
#
# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：
#
# 输入：[2,2,2,0,1]
# 输出：0

class Solution():
    def find_min(self, nums):
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left >> 1)
            if nums[mid] >= nums[left]:  # left 到 mid 完全有序
                if nums[mid] <= nums[right]:  # 如果此时mid 还小于right ，说明 left < mid < rigt 及 left 到mid都完全有序
                    return nums[left]
                else:
                    left = mid + 1  # 最小值在右边
            else:  # 一定有旋转，那么mid的左边一定有值
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                right = mid - 1
        return None


from random import randint

solu = Solution()
nums = sorted([randint(-10, 10) for _ in range(randint(1, 10))])
trans_idx = randint(0, len(nums) - 1)
print("ori_nums:", nums)
nums = nums[trans_idx:] + nums[:trans_idx]
print("nums:", nums)
print("res:", solu.find_min(nums))
