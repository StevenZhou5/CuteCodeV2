class Solution(object):
    def __init__(self):

        pass

    def merge_(self, nums):
        if not nums:
            return []
        nums = sorted(nums, key=lambda item: item[1])
        print("sorted:", nums)
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i][0] > res[-1][1]:
                res.append(nums[i])
            else:
                res[-1] = [min(nums[i][0], res[-1][0]), max(nums[i][1], res[-1][1])]
        return res


solu = Solution()
from random import randint

nums = list(map(lambda a: [a, a + randint(1, 5)],
                [randint(-10, 10) for _ in range(randint(0, 10))]))
print("origin", nums)
print("res:", solu.merge_(nums))
