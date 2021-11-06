class DynamicProgramming(object):
    def __init__(self):
        super(DynamicProgramming, self).__init__()

    def sum_latest(self, nums, target_num):
        """
        """
        if not nums or not target_num:
            return 0
        n = len(nums)
        # P[i][j] = p[i-1][j-wi] + wi
        P = [[0] * (target_num + 1) for _ in range(n + 1)]
        print("origin P:", P)
        for i in range(1, n + 1):
            for j in range(1, target_num + 1):
                wi = nums[i - 1]
                if wi <= j:  # 如果第i个物品的重量小于等于当前背包容量j
                    P[i][j] = max((P[i - 1][j - wi] + wi), (P[i - 1][j]), (P[i][j - 1]))
                else:
                    P[i][j] = max((P[i - 1][j], P[i][j - 1]))
        print("final P", P)
        return P[-1][-1]  # 最后一个一定是最大值

    def sum_latest_just_use_list(self, nums, target):
        if not nums or not target:
            return 0

        P = [0] * (target + 1)
        for i in range(len(nums)):
            cur_val = nums[i]
            # print(P)
            p = [0] * (target + 1)
            for j in range(1, target + 1):
                if j < cur_val:  # 容量j的背包装不下当前物品i
                    p[j] = max(P[j], P[j - 1])
                else:
                    # print(cur_val, j - cur_val)
                    p[j] = max(P[j], P[j - 1], (P[j - cur_val] + cur_val))
            P = p
        # print(P)
        return P[-1]

    def stock1(self, nums):
        "买卖无限次，收益最大"
        if not nums:
            return 0
        p0 = 0  # 第一天过后没有持有股票的最大收益
        p1 = -nums[0]  # 第一天过后持有股票的最大收益
        for i in range(1, len(nums)):
            p0, p1 = max(p0, p1 + nums[i]), max(p1, p0 - nums[i])  # 不操作 / 买了股票(前一天必须持有股票) # 不操作 / 买进股票(前一天必须没有持有股票)

        return max(p0, p1)

    def stock2(self, nums):
        "买入需要冻结一天"
        if not nums:
            return 0
        p0 = 0  # 可以买入
        p1 = -nums[0]  # 持有，但是冻结，不可卖出
        p2 = float("-inf")  # 持有，但是可以卖出
        for i in range(1, len(nums)):
            # print(p0, p1, p2)
            p0, p1, p2 = max(p0, (p2 + nums[i])), (p0 - nums[i]), max(p1, p2)

        return max(p0, p1, p2)

    def stock3(self, nums):
        "只能买卖一次，收益最大"
        if not nums:
            return 0
        res = 0
        cur_min = nums[0]
        for i in range(len(nums)):
            res = max(res, nums[i] - cur_min)
            cur_min = nums[i] if nums[i] < cur_min else cur_min

        return res


from random import randint

dp = DynamicProgramming()
nums, target_num = [randint(3, 9) for _ in range(5)], randint(0, 15)
# nums, target_num = [5, 6, 8, 8, 7], 13
print(nums, target_num)
print("res:", dp.sum_latest(nums, target_num))
print("res2:", dp.sum_latest_just_use_list(nums, target_num))

print("stick1 max_val:", dp.stock1(nums))
print("stick2 max_val:", dp.stock2(nums))
print("stick3 max_val:", dp.stock3(nums))
