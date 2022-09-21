# 2334. 元素值大于变化阈值的子数组
# 给你一个整数数组 nums 和一个整数 threshold 。
#
# 找到长度为 k 的 nums 子数组，满足数组中 每个 元素都 大于 threshold / k 。
#
# 请你返回满足要求的 任意 子数组的 大小 。如果没有这样的子数组，返回 -1 。
#
# 子数组 是数组中一段连续非空的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,4,3,1], threshold = 6
# 输出：3
# 解释：子数组 [3,4,3] 大小为 3 ，每个元素都大于 6 / 3 = 2 。
# 注意这是唯一合法的子数组。
# 示例 2：
#
# 输入：nums = [6,5,6,5,8], threshold = 7
# 输出：1
# 解释：子数组 [8] 大小为 1 ，且 8 > 7 / 1 = 7 。所以返回 1 。
# 注意子数组 [6,5] 大小为 2 ，每个元素都大于 7 / 2 = 3.5 。
# 类似的，子数组 [6,5,6] ，[6,5,6,5] ，[6,5,6,5,8] 都是符合条件的子数组。
# 所以返回 2, 3, 4 和 5 都可以。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], threshold <= 109

# class UnionFind():
#     def __init__(self, n):
#         self.root = list(range(n))
#         self.rank = [1] * n
#         self.lens = [1] * n

#     def find(self, i):
#         if self.root[i] != i:
#             self.root[i] = self.find(self.root[i])
#         return self.root[i]

#     def union(self, x, y):
#         x_root = self.find(x)
#         y_root = self.find(y)
#         if x_root != y_root:
#             if self.rank[x_root] < self.rank[y_root]:
#                 x_root, y_root = y_root, x_root
#             self.root[y_root] = x_root
#             self.lens[x_root] += self.lens[y_root] # 更新连续长度
#             if self.rank[x_root] == self.rank[y_root]:
#                 self.rank[x_root] += 1
#         return self.lens[x_root]

#     def get_len(self, i):
#         return self.lens[self.find(i)]

class Solution:
    def validSubarraySize(self, nums: [int], threshold: int) -> int:
        # 并查集:题目要求返回任意一组就ok，那么我们从最大的元素开始找，找到的元素就用并查集将其合并；后续没次访问的新数一定比之前所有的访问过的数都小，将其用并查集快速和两边合并后，只要新加入的num > threshold / k ,那么就找到了；
        # 时间复杂度：O(n * α(n)), n位nums的长度，因为并查集采用了按秩合并，α阿克曼函数的反函数，α(n)可以认为是一个很小的常数；
        # 空间复杂度：O(n)
        # n = len(nums)
        # union_find = UnionFind(n)

        # visted_idx = set()
        # for num, idx in sorted(zip(nums, range(n)),reverse = True):
        #     # print(num,idx)
        #     if idx + 1 in visted_idx: # 看下右边的元素是否已经访问过了，访问过就合并右边
        #         union_find.union(idx + 1, idx)
        #     if idx - 1 in visted_idx: # 看下左边的元素是否已经访问过了，访问过就合并左边
        #         union_find.union(idx, idx -1)
        #     visted_idx.add(idx)
        #     cur_len = union_find.get_len(idx)
        #     if num > (threshold / cur_len ):
        #         # print(union_find.root)
        #         return cur_len

        # return -1

        # 单调栈：假设每个元素i都是当前子数组中的最小值，那么只要这个最小值 > threshold / k[i]; 关键就是确定元素i能构成的k[i]的长度，那么暴力做法就是往两边扩；而加速办法就是从左到右用单调递增栈找到每个i的左边界，在从右到左找到每个i的右边界；那么就可以在O(n)时间复杂度内解决问题
        # 时间复杂度：O(n), 三次循环
        # 空间复杂度：O(n),
        n = len(nums)
        left_boand = [-1] * n  # 在nums[i] 左边第一个比nums[i] 小的数的索引
        left_stack = []
        for i, num in enumerate(nums):
            while left_stack and nums[left_stack[-1]] >= num:
                left_stack.pop()
            if left_stack:
                left_boand[i] = left_stack[-1]
            left_stack.append(i)

        right_boand = [n] * n  # 在nums[i] 右边第一个比nums[i] 小的数索引
        right_stack = []
        for i in range(n - 1, -1, -1):
            while right_stack and nums[right_stack[-1]] >= nums[i]:
                right_stack.pop()
            if right_stack:
                right_boand[i] = right_stack[-1]
            right_stack.append(i)

        # print(left_boand, right_boand)
        for i, num in enumerate(nums):
            cur_len = right_boand[i] - left_boand[i] - 1
            if num > threshold / cur_len:
                return cur_len
        return -1
