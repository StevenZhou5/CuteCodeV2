# 75. 颜色分类
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 必须在不使用库的sort函数的情况下解决这个问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
#
#
# 进阶：
#
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 桶排序
        # 时间复杂度： O(n), 需要遍历两次
        # 空间复杂度： O(1)
        # r_cnt, w_cnt= 0, 0
        # for num in nums:
        #     if num == 0:
        #         r_cnt += 1
        #     elif num == 1:
        #         w_cnt += 1
        # # print(r_cnt, w_cnt)
        # w_cnt += r_cnt #
        # for i in range(len(nums)):
        #     if i < r_cnt:
        #         nums[i] = 0
        #     elif i <  w_cnt:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2

        # 双指针：
        # 时间复杂度：O(n)，只需遍历一次
        # 空间复杂度：O(1)，需要遍历两次
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:  # 如果p2本身就是2，那么需要将p2左移，直到找到p2不为2的位置进行交换
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[
                i] == 0:  # 因为外层循环是从左到右，只要遇到 i == p0 且 nums[i]的时P0一定会后移，直到P0指向的是一个非0的数，所以不需要P2的处理；反过来如果外层是从后向前遍历的话，就需要对P0做判断了
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
