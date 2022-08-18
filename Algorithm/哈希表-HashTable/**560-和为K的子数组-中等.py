# 560. 和为 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        res = 0
        n = len(nums)
        pre_sum_count_map = {0: 1}
        pre_sum = 0  # 所有前面的数字加起来的总和，
        for i in range(n):
            pre_sum += nums[i]  # 一边循环计算新的pre_sum

            # print(pre_sum_count_map)
            # 一边用字典记录所有前缀和出现的次数，从i到j的连续数字之和 = pre_sum[j] - pre_sum[i]; 要满足pre_sum[j] - pre_sum[i] = k;
            # 那么只需要知道与pre_sum[i] = pre_sum[j] - k  相等的前缀和总共出现过几次；比如当j=100时pre_sum = 100;此时K=90，当i = 3,5,7的时候pre_sum都为10，那么 pre_sum[10] = 3 即为当遍历到位置100时 3到100的和 、5到100的和 、7到100的和都为k；
            res += pre_sum_count_map.get(pre_sum - k, 0)

            pre_sum_count_map[pre_sum] = pre_sum_count_map.get(pre_sum, 0) + 1
        return res
