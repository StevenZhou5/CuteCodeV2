# 322. 零钱兑换
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
# 提示：
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        # 动态规划: 时间复杂度O(S*n); 空间复杂度O(S); S位amount的值，n位coins有几种面额值
        # step1：状态定义
        dp = [float('inf')] * (amount + 1)  # dp[i] 代表凑出i元所需要的最少硬币数
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
