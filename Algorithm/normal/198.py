# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

class Solution():

    def get_max_val(self, nums):
        if not nums:
            return 0
        # 定义状态，偷了这家可以获得的最大值
        dp1 = 0  # 初始没有办法偷
        dp2 = nums[0]  # 只有一家
        res = dp2
        for i in range(1, len(nums)):
            print("dp1:%d,dp2:%d;" % (dp1, dp2))
            dp1, dp2 = dp2, max(dp1 + nums[i], dp2)
            res = max(res, dp2)

        return res


solu = Solution()
from random import randint

nums = [randint(0, 10) for _ in range(randint(0, 10))]
print("nums:", nums)
print("res:", solu.get_max_val(nums))
