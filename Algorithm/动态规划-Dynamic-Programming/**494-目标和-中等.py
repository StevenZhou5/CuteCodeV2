# 494. 目标和
# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1
#
#
# 提示：
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        # 动态回归 + map
        # 时间复杂度 O(n * sum_cnt) sum_cnt 是使用前n个数最多可以构造出来的不同加和的个数
        # 空间复杂度 O(sum_cnt) 只存储上一个位置的状态即可
        # step 1 状态定义
        # dp = collections.defaultdict(int) # 存储用前i个数，可以构造出多少个值，每个值的个数是多少
        # dp[0] = 1
        # n = len(nums)
        # for i in range(n):
        #     cur_dp = collections.defaultdict(int)
        #     # 状态转移
        #     for num, count in dp.items():
        #         cur_dp[num + nums[i]] += count
        #         cur_dp[num - nums[i]] += count
        #     dp = cur_dp
        # return dp[target]

        # 动态规划 + 剪枝
        # 时间复杂度：O(n * (sums - target)), 因为动态规划外层循环n，内层循环 (sums - target)/ 2  + 1,
        # 空间复杂度：O(sums - target)，因为状态dp存储了(sums - target) / 2 + 1个元素
        # 设所有元素和为sums, 设要是的最终和为target是所有添加符号的元素和为 neg，那么剩余正数的和为 sums - neg;
        #  则有等式 (sums - neg) - neg = target, 整理的neg = (sums - target) / 2; neg 必须为正整数
        sums = sum(nums)
        neg = (sums - target) / 2
        if neg < 0 or neg != int(neg):
            return 0
        neg = int(neg)
        # print(neg)
        # 现在我们把问题简化成了找和neg的组合有多少种，变成了一个典型的0 / 1背包问题
        # step1 状态定义
        dp = [0] * (neg + 1)  # dp[i][j] 代表使用前i个数构造出和为j的方法有多少种，因为每次更新第i行时只用第i - 1行的数据，所以只存列状态
        dp[0] = 1
        n = len(nums)
        for i in range(n):
            # print(dp)
            for j in range(neg, -1, -1):  # 0 / 1背包问题，所以需要从后向前遍历; 因为nums[i] 可以为0，所以这里一定要遍历到0
                # step2：状态转移
                dp[j] = dp[j] if nums[i] > j else (dp[j] + dp[j - nums[i]])

        return dp[-1]
