# 179. 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
# 输入：nums = [10,2]
# 输出："210"
# 示例 2：
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义比较函数 + 排序：
        # 时间复杂度：O(n * log(n)),比较的复杂度O(1), 排序的复杂度n * log(n)
        # 空间复杂度：O(1)
        def compile(x, y):  # 自定义比较函数: 把组合后值更大的放在前面；
            return int(y + x) - int(x + y)  # -( int(x + y) - int(y + x)) 如果x + y 比 y + x 大的越多，x要越往后，最前面加上负号相当于翻转

        nums = sorted(map(str, nums), key=cmp_to_key(compile))
        # print(nums)
        return "".join(nums) if nums[0] != '0' else '0'
