# 464. 我能赢吗
# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。
#
# 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
#
# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
#
# 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
#
# 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
#
# 示例：
#
# 输入：
# maxChoosableInteger = 10
# desiredTotal = 11
#
# 输出：
# false
#
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

class Solution():

    # def can_i_win(self, maxChoosableInteger, desiredTotal):
    #     if maxChoosableInteger >= desiredTotal:
    #         return True
    #     # 状态压缩：我能赢吗？
    #     # 最后一轮要赢的话：剩余可选数字中的最大值 >= 还需要的值，此时赢
    #     # 倒数第二轮要赢的话：当前剩余值>max(可选值) + min(可选值),选一个最优值，使得下一轮的 max(可选值)< 剩余值 <= max(可选值) + min(可选值)，那么下轮自己选的时候必赢；
    #     # >倒数第三轮要赢的话：当前剩余值 > max(可选值) + min(可选值) + sec_max(可选值),选任何一个值后仍然会是的当前剩余值 > max(可选值) + min(可选值)；此时选最小值
    #     can_use_nums = [i for i in range(1, maxChoosableInteger + 1)]
    #     is_win = False
    #     while desiredTotal > 0 and can_use_nums:
    #         if can_use_nums[-1] >= desiredTotal:
    #             return not is_win
    #         if len(can_use_nums) < 2:  # 如果只有1个或者两个可选数，且最大值任然不大于等于目标数，那么取第一个就行了
    #             desiredTotal -= can_use_nums[0]
    #             can_use_nums.remove(can_use_nums[0])
    #             is_win = not is_win
    #             continue
    #
    #         if can_use_nums[0] + can_use_nums[-1] < desiredTotal <= can_use_nums[0] + can_use_nums[-1] + can_use_nums[
    #             -2]:
    #             target = desiredTotal - (can_use_nums[0] + can_use_nums[-1])
    #             # 用二分查找找到最接近目标值的值
    #             left_idx = 0
    #             rigth_idx = len(can_use_nums) - 1
    #             res_idx = 0
    #             while left_idx <= rigth_idx:
    #                 mid_idx = left_idx + (rigth_idx - left_idx >> 1)
    #                 if can_use_nums[mid_idx] == target:
    #                     res_idx = mid_idx
    #                     break
    #                 if can_use_nums[mid_idx] > target:
    #                     rigth_idx = mid_idx - 1
    #                 else:
    #                     left_idx = mid_idx + 1
    #             res_idx = rigth_idx
    #             desiredTotal -= can_use_nums[res_idx]
    #             can_use_nums.remove(can_use_nums[res_idx])
    #             is_win = not is_win
    #             continue
    #         desiredTotal -= can_use_nums[0]
    #         can_use_nums.remove(can_use_nums[0])
    #         is_win = not is_win
    #
    #     # 所有数都取完了，还是没有大于等于目标值
    #     return False

    def can_i_win_with_dp_sc(self, maxChoosableInteger, desiredTotal):
        # 状态压缩的核心：用二进制记录每一种状态出现的情况:
        # 000 代表全部没有选，001代表只选了第一个，010代表只选了第二个；011代表选了第一个和第二个；111代表选了第一个第二个和第三个
        # 状态定义，dp[i] 代表上面一种二进制组合状态下，此时先手的玩家是否可以获胜
        dp = {}

        def dfs(cur_state, cur_desiredTotal):
            print("cur_state:%d,cur_des:%d" % (cur_state, cur_desiredTotal))
            if cur_state in dp:  # 如果此状态已经有过，那么直接返回
                return dp[cur_state]

            for i in range(1, maxChoosableInteger + 1):
                i_state = 1 << (i - 1)
                if cur_state & i_state != 0:  # 说明i已经被选了
                    continue
                new_desiredTotal = cur_desiredTotal - i
                if new_desiredTotal <= 0:  # 只要有一种情况能赢，
                    dp[cur_state] = True
                    return True
                new_state = cur_state + i_state
                # 状态转义： 对方稳赢，我就稳输掉；对方稳输，我就稳赢
                if not dfs(new_state, new_desiredTotal):  # 只要有一种情况对方稳输
                    dp[cur_state] = True
                    return True
            # 当所有值都不能赢的情况下，
            dp[cur_state] = False
            return False

        res = dfs(0, desiredTotal)
        print(dp)
        return res


solu = Solution()
maxChoosableInteger = 10
desiredTotal = 22
print("maxChoosableInteger:%d; desiredTotal:%d;" % (maxChoosableInteger, desiredTotal))
# print("res:", solu.can_i_win(maxChoosableInteger, desiredTotal))
print("res:", solu.can_i_win_with_dp_sc(maxChoosableInteger, desiredTotal))
