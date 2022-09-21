# 46. 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        # 递归 + 回溯：
        # 时间复杂度: O(n * n!) 因为所有组合总共是n!个 ,我们需要将当前答案使用 O(n)O(n) 的时间复制到答案数组中，相乘得时间复杂度为O(n * n!)。
        # 空间复杂度：O(n) 答案不算，n是递归调用栈栈的深度；
        n = len(nums)
        res = []

        def recursion(start):
            # 递归终止条件
            if start == n - 1:
                res.append(nums.copy())
                return
            for i in range(start, n):  # 把start 和 后面的值逐个交换
                nums[start], nums[i] = nums[i], nums[start]
                recursion(start + 1)
                nums[i], nums[start] = nums[start], nums[i]  # 交换完后要回溯

        recursion(0)
        return res
