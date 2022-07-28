# 473. 火柴拼正方形
# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
#
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
#
# 示例 1:
#
# 输入: [1,1,2,2,2]
# 输出: true
#
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例 2:
#
# 输入: [3,3,3,3,4]
# 输出: false
#
# 解释: 不能用所有火柴拼成一个正方形。
# 注意:
#
# 给定的火柴长度和在 0 到 10^9之间。
# 火柴数组的长度不超过15。
class Solution():
    def can_get_square_dp_sc(self, nums):
        if not nums or len(nums) < 4:
            return False
        num_cnt = len(nums)
        total_len = sum(nums)
        side_len = total_len >> 2
        if side_len << 2 != total_len:  # 不能整除4
            return False
        # 用二进制表示状态：001 代表只用了第一根火柴，111代表用了前3跟火柴
        # 状态定义 dp[i] = (side_len_cnt,left_len): 代表使用二进制状态i下的火柴，组成了几条完整的边side_len_cnt，以及不足一条完整边的剩余长度综合left_len
        dp = {}

        def recursion(cur_state, side_len_cnt, left_len):
            # 递归终止条件
            if side_len_cnt == 4 and left_len == 0:
                return True
            if cur_state in dp:
                return dp[cur_state]

            # 处理逻辑
            for i in range(num_cnt):
                state_i = 1 << i  # 如果只有第i跟火柴被选，用二进制状态表示
                # 当前火柴被选了，跳过
                if state_i & cur_state != 0:
                    continue

                new_left_len = left_len + nums[i]
                # 当前火柴加上left_len超过了变成，跳过
                if new_left_len > side_len:
                    continue
                new_state = cur_state + state_i
                new_side_len_cnt = side_len_cnt

                # 当前边加入刚好构成一条新的完整边，更新完整边数量和剩余边长度
                if new_left_len == side_len:
                    new_side_len_cnt += 1
                    new_left_len = 0

                # 如果选了当前边可以凑成四条完整边的情况，那么当前状态有满足组合情况，返回True,并更新状态
                if recursion(new_state, new_side_len_cnt, new_left_len):
                    dp[cur_state] = True
                    return True

            # 在当前状态下，所有情况都不能满足，return False
            dp[cur_state] = False
            return False

        return recursion(0, 0, 0)


solu = Solution()
nums = [7, 2, 5, 6, 1, 3, 3, 5, 8]
print("nums:", nums)
print("res:", solu.can_get_square_dp_sc(nums))
