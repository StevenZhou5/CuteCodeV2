# 69. x 的平方根
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
# 示例 1：
#
# 输入：x = 4
# 输出：2
# 示例 2：
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
# 提示：
#
# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找：时间复杂度O(log n), 空间复杂度O(1)
        l, r, ans = 0, x, -1  # 注意，这道题一定要用ans来记录最终结果，因为mid在最后一步计算的时候不一定会满足mid * mid <= x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


        # 牛顿迭代法
        # if x == 0 :
        #     return 0
        # x0, C = float(x), float(x)
        # while True:
        #     xi = 0.5 * (x0 + C / x0)  # 核心是推导出这个公式
        #     if x0 - xi < 1e-7:
        #         break
        #     x0 = xi
        #
        # return int(x0)
