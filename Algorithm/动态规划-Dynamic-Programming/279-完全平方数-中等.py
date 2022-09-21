# 279. 完全平方数
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#
#
# 示例 1：
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
# 提示：
#
# 1 <= n <= 104

class Solution:
    def numSquares(self, n: int) -> int:
        # 利用四平方和定理：https://baike.baidu.com/item/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86
        # 时间复杂度：O(n ^ 0.5), 最差情况是答案为3的是否，需要遍历一次choice_nums
        # 空间复杂度：O（1）， 如果用set的话是O(n ^ 0.5)
        #  step1 ： 判断是否为1
        # sqrt_n = n ** 0.5
        # if sqrt_n == int(sqrt_n):
        #     return 1

        # # step2 ： 判断是否为 4
        # # 判断是否能表示为 4^k*(8m+7)
        # def check_answer4(x):
        #     while (x % 4 == 0):
        #         x = x >> 2
        #     return x % 8 == 7

        # if check_answer4(n):
        #     return 4

        # # step3 ： 判断是否为2
        # # choice_nums_set = set() # 可以用set来省去sqrt_left_num 的 开根号运算
        # for i in range(1, int(sqrt_n) + 1):
        #     sqrt_left_num = (n - i * i ) ** 0.5
        #     # choice_nums_set.add(cur_val) # 一定要先添加，因为另外一个数可以选自己
        #     # if n - cur_val in choice_nums_set:
        #     #     return 2
        #     if sqrt_left_num == int(sqrt_left_num):
        #         return 2

        # # step4：最后就一定是3
        # return 3

        # 动态规划 + 状态压缩：完全背包问题
        # 时间复杂度：O(n ^ 1.5), 因为可选的choice_nums的数量为n ^ 0.5 次方，然后剩下就是一个完全背包问题
        # 空间复杂度：O(n), 使用了状态压缩dp的空间复杂度为O(n), choice_num的空间复杂度为O(n ^ 0.5), 所以 总的空间复杂度= O(n) + O(n ^ 0.5) = O(n)
        sqrt_n = n ** 0.5
        if sqrt_n == int(sqrt_n):
            return 1
        choice_nums = [i * i for i in range(int(sqrt_n) + 1)]
        dp = list(range(n + 1))  # dp[j] 代表用钱i个数字构成j最少需要多少个数字；初始代表只用1来构成所有数字
        for i in range(2, len(choice_nums)):  # i从2开始即可
            for j in range(choice_nums[i], n + 1):  # 新增一个num后，不会影响之前比num小的数的组合
                dp[j] = min(dp[j], dp[j - choice_nums[i]] + 1)
        # print(choice_nums, dp)
        return dp[-1]
