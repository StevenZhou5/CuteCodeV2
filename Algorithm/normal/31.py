# 31. 下一个排列
# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
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
# 示例 4：
#
# 输入：nums = [1]
# 输出：[1]
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution(object):
    def __init__(self):
        pass

    def get_next(self, nums):
        if not nums or len(nums) == 1:
            return
        cnt = len(nums)
        # 找到 要换的那个值：从后往前第一个降序中小的那个值
        idx = -1
        for i in range(cnt - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break
        print(idx)
        if idx == -1:
            nums.reverse()
            return nums

        # 交换 idx 与 后面第一个大于它的值交换
        for i in range(cnt - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
                break
        print(nums)

        # idx 后面的数据翻转
        nums[idx + 1:] = nums[cnt:idx:-1]
        return nums


nums = [0, 1, 2, 3, 4, 7, 5, 6, 8, 9]
solu = Solution()
for i in range(10):
    print("res:", solu.get_next(nums))
