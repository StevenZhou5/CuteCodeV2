# 754. 到达终点数字
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
#
# 你可以做一些数量的移动 numMoves :
#
# 每次你可以选择向左或向右移动。
# 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
# 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
#
#
#
# 示例 1:
#
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
# 示例 2:
#
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#
#
# 提示:
#
# -109 <= target <= 109
# target != 0
class Solution:
    def reachNumber(self, target: int) -> int:
        # 数学转换： 从1 到 k 个数连加，考虑在那些数前面加负号
        # 时间复杂度：O(target ** 0.5)
        # 空间复杂度：O(1)
        target = abs(target)  #
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else (k + 1 + k % 2)
