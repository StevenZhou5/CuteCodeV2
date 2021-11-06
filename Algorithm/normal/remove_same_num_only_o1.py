class Solution(object):

    def __init__(self):
        pass

    def remove_same_num_only_01(self, nums):
        if not nums:
            return (nums, 0)

        idx_insert = 0
        idx_next_target = 0
        while idx_next_target < len(nums):
            if idx_next_target == 0 or nums[idx_next_target] != nums[idx_next_target - 1]:
                nums[idx_insert] = nums[idx_next_target]
                idx_insert += 1
                idx_next_target += 1
            else:
                idx_next_target += 1

        return (nums, idx_insert)

    def remove_target_num(self, nums, tag_num):
        if not nums:
            return (nums, 0)

        insert_idx2 = 0
        next_target_idx = 0
        while next_target_idx < len(nums):
            if nums[next_target_idx] == tag_num:
                next_target_idx += 1
            else:
                nums[insert_idx2] = nums[next_target_idx]
                # print("insert_idx:", insert_idx)
                insert_idx2 += 1
                next_target_idx += 1

        return (nums, insert_idx2)


from random import randint

solu = Solution()

nums = [randint(0, 10) for _ in range(randint(0, 20))]
nums = sorted(nums)
tar_num = randint(0, 10)
print(nums, tar_num, len(nums))
# print("res1:", solu.remove_same_num_only_01(nums))
print("res2:", solu.remove_target_num(nums, tar_num))
