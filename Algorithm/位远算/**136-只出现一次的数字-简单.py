# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # set()： 时间复杂度O(n), 空间复杂度O(n)
        # already_set = set()
        # for num in nums:
        #     if num in already_set:
        #         already_set.remove(num)
        #     else:
        #         already_set.add(num)
        # return already_set.pop()

        # 位运算： 异或运算的三条性质：x ^ 0 = x 、 x ^ x = 0 、异或运算满足结合率与交换率：a ^ b ^ c = a ^ (b ^ c) = a ^ c ^ b
        res = 0
        for num in nums:
            res ^= num
        return res
