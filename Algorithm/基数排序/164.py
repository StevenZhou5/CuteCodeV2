# 164. 最大间距
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
# 示例 2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
# 说明:
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

class Solution:

    def get_max_gap(self, nums):
        if not nums or len(nums) == 1:
            return 0
        cnt = len(nums)
        min_val = nums[0]
        max_val = nums[0]
        for i in range(1, cnt):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])

        # 最大间隔一定大于(max_val - min_val) // (cnt - 1) ,
        # 可以用反证法证明如果最大gap小于此值，那么min+(n-1)*gap < max ,与实际情况不符，所以最大间隔一定大于 (max_val - min_val) // (cnt - 1)
        bucket_size = (max_val - min_val) // (cnt - 1)
        bucket_list = [[-1, -1] for _ in range(cnt)]  # 用于存每个桶的最大值和最小值

        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            cut_bucket_min, cut_bucket_max = bucket_list[bucket_idx]
            if cut_bucket_min == -1:
                bucket_list[bucket_idx] = [num, num]
            else:
                bucket_list[bucket_idx] = [min(num, cut_bucket_min), max(num, cut_bucket_max)]
        print(bucket_list)
        # 最大间隔一定产生在不同桶中，所以我们从
        pre_max = min_val  # 初始的最大值一定是全局最小值
        res = 0
        for cur_min, cur_max in bucket_list:
            if cur_min == -1:
                continue
            res = max(cur_min - pre_max, res)  # 更新最大值：
            pre_max = cur_max

        return res


solu = Solution()
from random import randint

nums = [randint(1, 100) for _ in range(randint(1, 20))]
print("nums:", nums)
print("res:", solu.get_max_gap(nums))
