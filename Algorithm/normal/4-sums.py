class Solution(object):
    def __init__(self):
        pass

    def get_res(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        res = set()
        nums = sorted(nums)
        cnt = len(nums)
        for idx1 in range(cnt - 3):
            for idx2 in range(idx1, cnt - 2):
                idx3 = idx2 + 1
                idx4 = cnt - 1
                while idx3 < idx4:
                    sums = nums[idx1] + nums[idx2] + nums[idx3] + nums[idx4]
                    if sums == target:
                        res.add((nums[idx1], nums[idx2], nums[idx3], nums[idx4]))
                        idx3 += 1
                        while idx3 < idx4 and nums[idx3] == nums[idx3 - 1]:
                            idx3 += 1

                        idx4 -= 1
                        while idx4 > idx3 and nums[idx4] == nums[idx4 + 1]:
                            idx4 -= 1
                    elif sums < target:
                        idx3 += 1
                        while idx3 < idx4 and nums[idx3] == nums[idx3 - 1]:
                            idx3 += 1
                    else:
                        idx4 -= 1
                        while idx4 > idx3 and nums[idx4] == nums[idx4 + 1]:
                            idx4 -= 1
        return res


from random import randint

nums, target = [randint(-9, 9) for _ in range(10)], randint(-10, 10)
print(nums, target)
solu = Solution()
print(solu.get_res(nums, target))
