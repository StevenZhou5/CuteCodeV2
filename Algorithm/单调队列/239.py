# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
# 示例 3：
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
# 示例 4：
#
# 输入：nums = [9,11], k = 2
# 输出：[11]
# 示例 5：
#
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

class Solution():

    def get_window_max_val(self, nums, k):
        n = len(nums)
        if n < k:
            return []

        # 单调队列值存左边的最大值的idx
        from collections import deque
        queue = deque()
        queue.append(0)
        for i in range(1, k):
            if nums[i] > nums[queue[0]]:
                queue.clear()
            queue.append(i)
        print(queue)
        res = []
        res.append(nums[queue[0]])

        for i in range(k, n):
            if nums[i] > nums[queue[0]]:
                queue.clear()
            queue.append(i)
            res.append(nums[queue[0]])
        return res


solu = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print("res:", solu.get_window_max_val(nums, k))
