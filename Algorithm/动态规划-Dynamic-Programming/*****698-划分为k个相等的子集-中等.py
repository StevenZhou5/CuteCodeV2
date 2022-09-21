# 698. 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#
#
# 示例 1：
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 示例 2:
#
# 输入: nums = [1,2,3,4], k = 3
# 输出: false
#
#
# 提示：
#
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内
class Solution:
    def canPartitionKSubsets(self, nums: [int], k: int) -> bool:
        # 状态压缩dp + 位运算: 时间复杂度O(n * 2 ^ n)：外层循环2 ^ n , 内存循环n；
        sum_val = sum(nums)
        if sum_val % k:
            return False
        nums.sort()
        target_num = sum_val // k
        # print(nums)
        # print(target_num)
        if nums[-1] > target_num:
            return False

        n = len(nums)
        all_size = (1 << n)
        dp_binary = [False] * all_size  # 通过二进制数把所有组合都列出来，
        dp_binary[0] = True
        dp_sum = [0] * all_size

        for i in range(all_size):  # 遍历所有可能
            if not dp_binary[i]:  # 不满足条件的组合直接跳过
                continue

            for j in range(n):  # 在当前组合下，继续选择可选择的商品
                if (i >> j) & 1:  # 如果此商品已经被选了，则跳过
                    continue

                # 状态转义的判断是最核心的点
                if (dp_sum[i] % target_num) + nums[
                    j] <= target_num:  # 判断当前数是否可以加到此组合中，如果组合的余数 + 当前数 <= target_num ,说明可以将当前数放到某一组组合中，这也保证了余数一定是由完整的数组合得来的
                    # print(i, j, dp_sum[i], nums[j])
                    cur_binart_state = i | (1 << j)
                    dp_binary[cur_binart_state] = True
                    dp_sum[cur_binart_state] = dp_sum[i] + nums[j]
                else:  # 因为已经排过序，如果最小的数都加不进去，后面的就不用判断了
                    break
                    # print(dp_binary)

        return dp_binary[-1]
