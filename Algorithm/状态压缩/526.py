# 526. 优美的排列
# 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：
#
# perm[i] 能够被 i 整除
# i 能够被 perm[i] 整除
# 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：
# 第 1 个优美的排列是 [1,2]：
# - perm[1] = 1 能被 i = 1 整除
# - perm[2] = 2 能被 i = 2 整除
# 第 2 个优美的排列是 [2,1]:
# - perm[1] = 2 能被 i = 1 整除
# - i = 2 能被 perm[2] = 1 整除
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
# 提示：
#
# 1 <= n <= 15


class Solution():

    def get_beautiful_list_dp_sc(self, n):
        # 二进制状态表示：110 ： 选第二个数和第三个数构造了一个长度为2和优美队列
        # 状态定义
        dp = {}  # ()

        def recursion(cur_state, next_i):
            # 递归终止条件
            if next_i == n + 1:
                dp[(cur_state, next_i)] = 1
                return 1
            if (cur_state, next_i) in dp:  # 这种状态已经出现过了，
                return dp[(cur_state, next_i)]
            count = 0
            for i in range(1, n + 1):
                i_state = 1 << (i - 1)
                if i_state & cur_state != 0:  # 当前值被选了
                    continue
                if i % next_i != 0 and next_i % i != 0:  # 当前值不适合这个位置
                    continue
                new_state = cur_state + i_state
                count += recursion(new_state, next_i + 1)  # 把每一种选择后的数量都加上

            dp[(cur_state, next_i)] = count
            return count

        res = recursion(0, 1)
        print("dp:", dp)
        return res


solu = Solution()
print("res:", solu.get_beautiful_list_dp_sc(4))
