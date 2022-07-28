# 1425. 带限制的子序列和
# 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。
#
# 数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。
#
#
#
# 示例 1：
#
# 输入：nums = [10,2,-10,5,20], k = 2
# 输出：37
# 解释：子序列为 [10, 2, 5, 20] 。
# 示例 2：
#
# 输入：nums = [-1,-2,-3], k = 1
# 输出：-1
# 解释：子序列必须是非空的，所以我们选择最大的数字。
# 示例 3：
#
# 输入：nums = [10,-2,-10,-5,20], k = 2
# 输出：23
# 解释：子序列为 [10, -2, -5, 20] 。
#
#
# 提示：
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
class Solution():

    # 暴力的动态规划
    def get_max_val(self, nums, k):
        n = len(nums)
        # 状态定义 dp[i] 表是选择第i个数作为结尾所能得到的最大值
        dp = []
        res = float('-inf')
        for i in range(n):
            cur_val = nums[i]
            for j in range(len(dp) - 1, max(len(dp) - k - 1, -1), -1):
                print(j)
                cur_val = max(cur_val, dp[j] + nums[i])
            dp.append(cur_val)
            res = max(res, cur_val)
        print(dp)
        return res
    #动态规划 + 单调队列
    def constrainedSubsetSum(self, nums, k: int) -> int:
        n = len(nums)
        # 状态定义：dp[i] 代表以第i个数为最后一个数，形成的最大子序列和
        dp = [nums[0]]
        from collections import deque
        # 用单调队列来存储dp中最近K个中最大的值的索引
        max_index_queue = deque()
        max_index_queue.append(0)
        res = nums[0]
        for i in range(1, n):
            # print("1:",max_index_queue)
            if i - max_index_queue[0] > k:
                max_index_queue.popleft()
            # print("2:",max_index_queue)
            cur_val = max(nums[i], dp[max_index_queue[0]] + nums[i])
            dp.append(cur_val)
            while max_index_queue and dp[max_index_queue[-1]] < cur_val:
                max_index_queue.pop()
            max_index_queue.append(i)
            res = max(cur_val, res)
        print(dp)
        return res


solu = Solution()
# nums = [randint(-10000, 10000) for _ in range(10)]
nums = [10, -2, -10, -5, 20]
k = 2
print("nums:", nums)
print("res:", solu.get_max_val(nums, k))
