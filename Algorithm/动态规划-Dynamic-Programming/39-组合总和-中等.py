# 39. 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#
#
#
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例 2：
#
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：
#
# 输入: candidates = [2], target = 1
# 输出: []
#
#
# 提示：
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都 互不相同
# 1 <= target <= 500

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        # 动态规划;完全背包问题, 不用额外考虑多次使用某个值的情况，因为在动态规划的过程中已经把多次使用某个值包含进去了
        # 时间复杂度：O(n * target) 外层循环n, 内层循环 target
        # 空间复杂度：O(target * s) s为1-target中每个值的组合数
        n = len(candidates)
        # step1: 状态的定义
        dp = [[] for _ in range(target + 1)]  # dp[j] 代表只用前i个元素构成目标j所有的可能的list,
        for i in range(n):
            for j in range(1, target + 1):  # 从前往后遍历是完全背包问题可以选无数个，从后往前遍历就变成了0/1背包问题，最多只能选1次
                cur_sum = candidates[i]
                if cur_sum == j:  # 当前候选值就等于i 直接添加
                    dp[j].append([cur_sum])
                elif cur_sum < j:  # 当前候选值小于 j,
                    left_num = j - cur_sum
                    for sum_list in dp[
                        left_num]:  # 这里循环的时候就已经把多次使用cur_sum的情况考虑进去了，所以不需要再额外考虑使用多个cur_sum的情况：当候选值为2时，j = 2 时为[2]， j = 4是 为dp[4] = dp[2] + [2] 此时使用了两次2， j = 6 时 为 dp[6] = dp[4] + [2]
                        # step2：状态转义方程
                        dp[j].append(sum_list + [cur_sum])

                        # print(dp)
        return dp[-1]
