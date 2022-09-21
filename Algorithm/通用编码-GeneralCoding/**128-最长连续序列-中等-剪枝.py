# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        # 递归(DFS) + 记忆化
        # 时间复杂度O(n): 每个数访问记录一次
        # 空间复杂度O(n): 需要记录每个访问过的数
        # n = len(nums)
        # nums_set = set(nums)
        # visted_nums_map = {}
        # def get_max_len(num):
        #     # print(num, visted_nums_map)
        #     if num not in nums_set:
        #         return 0
        #     if num in visted_nums_map:
        #         return visted_nums_map[num]
        #     max_len = 1 + get_max_len(num - 1) # 这里向上找或者向下找够可以
        #     visted_nums_map[num] = max_len
        #     return max_len
        # res = 0
        # for num in nums_set:
        #     if num in visted_nums_map: # 不需要判断已经访问过的数
        #         continue
        #     # print(num)
        #     res = max(res, get_max_len(num))
        # return res

        # 使用栈模拟递归：
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # nums_set = set(nums)
        # # step1:状态定义
        # dp_map = {} # dp[i] 代表以i作为结尾的最长连续子数组的长度
        # res = 0
        # for num in nums_set:
        #     if num in dp_map:
        #         continue
        #     max_len = 0
        #     stack = [num]
        #     pre_num = stack[-1] - 1
        #     while pre_num in nums_set:
        #         if pre_num in dp_map:
        #             max_len = dp_map[pre_num]
        #             break
        #         stack.append(pre_num)
        #         pre_num -= 1
        #     while stack:
        #         max_len += 1
        #         # step2：状态的转移
        #         dp_map[stack.pop()] = max_len

        #     res = max(res, max_len)
        # return res

        # 剪枝： 从每个最左端元素遍历
        # 时间复杂度：O(n), 生成set O(n), 遍历是每个元素最多判断两次外层循环一次，内存循环一次 O(n) + O(n)， 总时间复杂度 3 * O(n) = O(n)
        # 空间复杂度：O(1)
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:  # 剪枝，只从连续区间的最小值进行遍历
                cur_len = 1
                while num + 1 in nums_set:
                    cur_len += 1
                    num += 1
                res = max(cur_len, res)
        return res
