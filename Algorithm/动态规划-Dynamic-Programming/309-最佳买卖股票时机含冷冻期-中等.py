# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1:
#
# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 示例 2:
#
# 输入: prices = [1]
# 输出: 0
#
#
# 提示：
#
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # 动态规划：时间复杂度O(n); 空间复杂度O(1);
        # step1: 状态定义
        pre_have = float('-inf')  # 当天操作完后持有股票
        pre_empty = 0  # 当天操作完后不持有股票，且不在冷冻期
        pre_code = float('-inf')  # 当前操作完后不持有股票，且在冷冻期
        for price in prices:
            # print(pre_have, pre_empty, pre_code)
            # step2：状态转移方程
            pre_have, pre_empty, pre_code = max(pre_have, pre_empty - price), max(pre_empty, pre_code), pre_have + price
        return max(pre_empty, pre_code)  # 最终结果
