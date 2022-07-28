# 698. 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
# 示例 1：
# 
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
#
# 提示：
#
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000

class Solution():
    # 和火柴构造正方形一样
    def can_get(self, nums, k):
        if len(nums) < k:
            return False
        total = sum(nums)

        if total % k != 0:
            return False
        side_len = total // k
        # 和火柴构造正方形一样的状态定义
        # 状态定义，dp[101] = (complete_cnt,left_len) 情况下是否能完成分割；代表选择第一个数和第三个数是，能够凑出来的完整边数目以及不完整边的剩余len
        # 比如[1,2,3] 要分成2条边,边长为3； 那么dp[101] = (1,1) 就代表用[1][3] 可以构造出一条完整边3，还多余1就是不完整边的长度
        len_nums = len(nums)
        dp = {}

        def recursion(cur_state, side_cnt, left_len):
            # 递归终止条件，所有
            if side_cnt == k:  #
                dp[cur_state] = True
                return True
            if cur_state in dp:
                return dp[cur_state]

            for i in range(len_nums):
                i_state = (1 << i)
                if i_state & cur_state != 0:  # 说明此位置的数已经被选了
                    continue
                new_left_len = left_len + nums[i]
                if new_left_len > side_len:  # 如果选了，加上left超出边长，那么不能选
                    continue
                new_state = cur_state + i_state
                new_side_cnt = side_cnt
                if new_left_len == side_len:  # 当刚好凑出一条完整边时，更新new_side_cnt 和 new_left_len
                    new_side_cnt += 1
                    new_left_len = 0
                if recursion(new_state, new_side_cnt, new_left_len):  # 只要有一种组合可以满足，那么此状态就有解，返回True
                    dp[cur_state] = True
                    return True
            # 所有情况都不行，返回False
            dp[cur_state] = False
            return False

        res = recursion(0, 0, 0)
        print("dp:", dp)
        return res


solu = Solution()
nums, k = [4, 3, 2, 3, 5, 2, 1, 5], 5
print("res:", solu.can_get(nums, k))
