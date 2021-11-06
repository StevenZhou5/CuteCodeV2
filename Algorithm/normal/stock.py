class Solution(object):

    def __init__(self):
        pass

    def only_one(self, nums):
        if not nums or len(nums) == 1:
            return 0
        max_val = 0
        cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_min, max_val = min(cur_min, nums[i]), max(max_val, nums[i] - cur_min)

        return max_val

    def no_limit(self, nums):
        if not nums or len(nums) == 1:
            return 0
        p0 = 0  # 不持有
        p1 = -nums[0]  # 持有
        for i in range(1, len(nums)):
            p0, p1 = max(p0, p1 + nums[i]), max(p1, p0 - nums[i])

        return max(p0, p1)

    def only_k(self, nums, k):
        if not nums or len(nums) == 1 or k <= 0:
            return 0
        p0 = [float("-inf")] * (k + 1)
        p0[0] = 0  # 交易0次，且不持有股票
        p1 = [float("-inf")] * (k + 1)
        p1[1] = -nums[0]  # 交易一次，且持有股票
        print(p0, p1)
        for i in range(1, len(nums)):
            for j in range(min(k + 1, i >> 1 + 1)):
                p0[j], p1[j] = max(p0[j], p1[j] + nums[i]), max(p1[j], p0[j - 1] - nums[i] if j > 0 else float('-inf'))
            # print("i:", p0, p1)
        return max(max(p0), max(p1))


solu = Solution()
from random import randint

nums = [randint(1, 10) for _ in range(10)]
print("nums:", nums)
print("only_one:", solu.only_one(nums))
print("no_limit:", solu.no_limit(nums))
print("only_k:", solu.only_k(nums, 2))
