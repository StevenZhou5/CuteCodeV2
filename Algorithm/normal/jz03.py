# 剑指 Offer 03. 数组中重复的数字
# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
#
# 限制：
#
# 2 <= n <= 100000

class Solution():
    def find_repeat_num(self, nums):
        if not nums:
            return None
        for num in nums:  # 因为所有数字都在0—n-1之间，所以可以利用原数组的位置来代表是否有重复，如果有重复，就把对应位置的元素变为负数
            if num == -1:
                num = 0
            abs_num = abs(num)
            if nums[abs_num] < 0:  # 说明此位置之前已经有过值了
                return abs(num)

            nums[abs_num] = -1 if nums[abs_num] == 0 else -nums[abs_num]
            print(nums)
        return None

    def find_first_positive_num(self, nums):
        if not nums:
            return None
        n = len(nums)
        # step1:把小于等于0的值变为n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # 把能找到的正数的对应索引位置的数变为负数
        for num in nums:
            abs_num = abs(num)
            if abs_num < n and nums[abs_num] > 0:
                nums[abs_num] = - nums[abs_num]
                # 从1开始找，第一个值大于0的位置的数就是第一个没有出现的正数
        for i in range(1, n):
            if nums[i] > 0:
                return i
        return n  # 所有都出现了，那么下一个就是n


solu = Solution()
from random import randint

nums = [randint(-9, 9) for _ in range(10)]
# nums = [6, 3, 1, 0, 2, 5, 3]
print("nums:", nums)
# print("res:", solu.find_repeat_num(nums))
print("find_first_positive_num", solu.find_first_positive_num(nums))
