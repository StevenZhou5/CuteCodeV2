# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution():
    def get_max_continue_len(self, nums):
        if not nums:
            return 0
        dp = {}
        max_len = 0
        for num in nums:
            if num in dp:  # 如果已经出现过，不需要再计算了
                continue
            dp_num_pre = dp.get(num - 1,
                                0)  # 如果没有出现过它的值为0，后续会被当前num更新；如果它的值为1，那么他的值会在dp[num - dp_num_pre]时更新，后续只有num-2出现时才会用到它，此时它也被更新了；如果它的值>1.那么以后没有人会用它了，不用更新,只用更新dp[num - dp_num_pre],因为只有它以后才有机会被用到；
            dp_num_next = dp.get(num + 1, 0)
            cur_len = dp_num_pre + dp_num_next + 1

            max_len = max(max_len, cur_len)

            dp[num] = cur_len
            dp[num - dp_num_pre] = cur_len  # 把起点索引的值赋值为当前长度，
            dp[num + dp_num_next] = cur_len  # 把终点索引的值赋值为当前长度
            print(dp)

        return max_len


# nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [4, 3, 2, 1, 5, 6]
print("nums:", nums)
solu = Solution()
print("res:", solu.get_max_continue_len(nums))
