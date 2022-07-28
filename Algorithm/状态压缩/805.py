# 805. 数组的均值分割
# 给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）
#
# 返回true ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。
#
# 示例:
# 输入:
# [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
# 注意:
#
# A 数组的长度范围为 [1, 30].
# A[i] 的数据范围为 [0, 10000].

class Solution():
    def is_can_split_dp_sc(self, nums):
        # 状态定义：dp[state] 表示在当前分割状态下是否满足题目要求
        # state 用二进制表示， 假设nums的长度为5; 11001 表示B数组选[nums[0],nums[3],nums[4] ],C数组选[nums[1],nums[2]]的状态
        dp = {}
        len_nums = len(nums)

        def recursion(cur_state, sum_b, b_cnt, sum_c, c_cnt):
            # 递归终止条件
            if b_cnt > 0 and c_cnt > 0 and (sum_b / b_cnt == sum_c / c_cnt):
                dp[cur_state] = True
                return True

            if cur_state in dp:
                return dp[cur_state]

            # 依次向B中加入一个新元素
            for i in range(len_nums):
                i_state = 1 << i
                if cur_state & i_state != 0:  # i位置已经被选，跳过
                    continue
                new_state = cur_state + i_state
                new_sum_b = sum_b + nums[i]
                new_b_cnt = b_cnt + 1
                new_sum_c = sum_c - nums[i]
                new_c_cnt = c_cnt - 1
                if recursion(new_state, new_sum_b, new_b_cnt, new_sum_c, new_c_cnt):  # 只要后续有一种情况满足，即可返回
                    dp[cur_state] = True
                    return True
            # 所有情况都无法满足，此状态为False
            dp[cur_state] = False
            return dp[cur_state]

        res = recursion(0, 0, 0, sum(nums), len_nums)
        print(dp)
        return res


solu = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("res:", solu.is_can_split_dp_sc(nums))
