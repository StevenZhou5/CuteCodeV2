# 912. 排序数组
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
# 提示：
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
class Solution:
    def sortArray(self, nums):
        if not nums or len(nums) == 1:
            return nums
        min_val = max_val = nums[0]
        bucket_map = {}
        for num in nums:
            min_val = min(num, min_val)
            max_val = max(num, max_val)
            cur_num_cnt = bucket_map.setdefault(num, 0)
            bucket_map[num] = cur_num_cnt + 1
        print(bucket_map)
        res = []
        for num in range(min_val, max_val + 1):
            cur_num_cnt = bucket_map.get(num, 0)
            res += [num] * cur_num_cnt

        return res

    def sortArrayV2(self, nums):
        # 优化空间复杂度:用完就扔
        if not nums:
            return nums
        min_val = float('inf')
        max_val = float('-inf')
        counter_map = {}
        while nums:
            cur_val = nums.pop()
            min_val = min(min_val, cur_val)
            max_val = max(max_val, cur_val)
            cur_val_cnt = counter_map.setdefault(cur_val, 0)
            counter_map[cur_val] = cur_val_cnt + 1
        print("min_val: %d; max_val: %d" % (min_val, max_val))
        print("counter_map:", counter_map)
        for num in range(min_val, max_val + 1):
            if counter_map.get(num, 0) == 0:
                continue
            nums += [num] * counter_map.pop(num)
        return nums


solu = Solution()
from random import randint

nums = [randint(-5, 5) for _ in range(randint(0, 10))]
print("nums:", nums)
# print("res:", solu.sortArray(nums))
print("res:", solu.sortArrayV2(nums))
