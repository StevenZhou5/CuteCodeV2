# 55. 跳跃游戏
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] <= 105

class Solution():
    def jump_game(self, nums):
        if not nums:
            return False
        n = len(nums)
        # 状态定义：当前位置是否可达
        dp = [False] * n
        dp[0] = True  # 初始状态0位置可达，其他暂时都不可达

        for i in range(n):
            # 如果当前位置可达 并且 下一个位置不越界，才可以通过它跳走
            if not dp[i]:
                continue
            for next in range(1, nums[i] + 1):
                if i + next < n:
                    dp[i + next] = True  # 状态转义: 下一个可以跳到的位置为True
        print("all_dp:", dp)
        return dp[-1]


solu = Solution()

# nums = [randint(1, 4) for _ in range(randint(0, 10))]
nums = [5, 1, 0, 0, 0, 1, 1]
print("nums:", nums)
solu.jump_game(nums)
