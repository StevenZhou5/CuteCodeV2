# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同

class Solution():
    def get_all_with_binary(self, nums):
        if not nums:
            return [[]]
        # 状态压缩
        # 000,001，010，011，100，101，110，111 全组合正好对二进制为的所有组合0-2^n
        n = len(nums)
        res = []
        for i in range((1 << n)):  # 1-2^n-1
            cur_res = []
            for j in range(n):
                if (i >> j) & 1 == 1:  # 对应二进制为为 1 的话，则需要加入当前位置元素
                    cur_res.append(nums[j])
            # print("i:", i, "; cur_res:", cur_res)
            res.append(cur_res)
        return res


from random import randint

nums = [randint(-10, 10) for _ in range(randint(0, 4))]
nums = list(set(nums))
print("nums:", nums)
solu = Solution()
print("res_get_all_with_binary:", solu.get_all_with_binary(nums))
