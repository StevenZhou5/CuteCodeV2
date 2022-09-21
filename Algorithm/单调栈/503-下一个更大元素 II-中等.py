# 503. 下一个更大元素 II
# 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
#
# 数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 示例 2:
#
# 输入: nums = [1,2,3,4,3]
# 输出: [2,3,4,-1,4]
#
#
# 提示:
#
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109

class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        # 暴力解法
        # 时间复杂度： O(n * n) 外层循环n 次， 内层循环n 次
        # 空间复杂度：O(1), res不算，不需要额外存储空间
        # res = []
        # n = len(nums)
        # for i in range(n):
        #     j = i + 1
        #     for _ in range(n - 1):
        #         cur_idx = j % n
        #         # print(i, cur_idx)
        #         if nums[cur_idx] > nums[i]:
        #             res.append(nums[cur_idx])
        #             break
        #         j += 1
        #     else:
        #         res.append(-1)

        # return res

        # 单调栈
        # 时间复杂度：O(n) , 两次循环，每次循环n次，最多入栈一次，出栈一次，总共不会超过4n
        # 空间复杂度：O(n) , 需要一个单调栈来存储单调递减的元素
        n = len(nums)
        stack = [0]  # 单调递减栈
        res = [-1] * n
        # 第一次循环既要出栈，又要入栈
        for i in range(1, n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]  # 出栈的时候跟下出栈元素的结果，因为是单调递减栈，所以出栈时nums[i]一定是第一个大于出栈位置元素的值
            stack.append(i)  # 第一循环所有元素都要入栈
        if not stack:
            return res
            # 第二次循环只出栈，不入栈
        for i in range(stack[0] + 1):  # 只用看到最大值前面的位置即可，因为stack[0]是栈内最大值，它一定可以将栈内剩余的值全部弹出了
            if not stack:
                break
            while nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]

        return res
