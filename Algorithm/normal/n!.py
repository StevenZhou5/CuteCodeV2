class Soultion(object):
    def __init__(self):
        pass

    def get_res(self, nums):
        if not nums:
            return []
        self.res = []  # 如果nums 有重复，改为set
        self.get_all(0, nums)
        return self.res

    def get_all(self, idx, nums):
        if idx == len(nums):
            self.res.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.get_all(idx + 1, nums)
            nums[idx], nums[i] = nums[i], nums[idx]


sou = Soultion()
nums = [str(i) for i in range(3)]
print("origin:", nums)
print(sou.get_res(nums))
