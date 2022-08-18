# 31. 下一个排列
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 示例 2：
#
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 示例 3：
#
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两边扫描： 时间复杂O(n)； 空间复杂度O(1)-使用左右结点交换，O(n)-使用系统方法
        # step1:从后向前找到第一个比前一个大的数
        n = len(nums)
        target_idx = 0
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                target_idx = i
                break
        # print(taget_idx)
        # step2:从目标数后面的数开始重新排列:从小到大，不用真的排序，只要翻转一下就就是从小到大了
        # nums[target_idx:] = reversed(nums[target_idx:]) # 直接调用系统方法,空间复杂度O(n) - 因为需要一个临时的nums[target_idx:] 数组
        left, right = target_idx, n - 1  # 空间复杂度O(1)的自定义翻转
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # step3: 从目标数开始向后遍历，找到第一个比 target_idx - 1 位置上大的数和 target - 1 位置上的数进行交换
        for j in range(target_idx, n, 1):
            if nums[j] > nums[target_idx - 1]:
                nums[j], nums[target_idx - 1] = nums[target_idx - 1], nums[j]
                return
