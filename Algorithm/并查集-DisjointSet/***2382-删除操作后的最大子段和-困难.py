# 2382. 删除操作后的最大子段和
# 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标 removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
#
# 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
#
# 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
#
# 注意：一个下标至多只会被删除一次。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
# 输出：[14,7,2,2,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。
# 查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。
# 查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。
# 查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。
# 查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [14,7,2,2,0] 。
# 示例 2：
#
# 输入：nums = [3,2,11,1], removeQueries = [3,2,1,0]
# 输出：[16,5,3,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。
# 查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。
# 查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。
# 查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [16,5,3,0] 。
#
#
# 提示：
#
# n == nums.length == removeQueries.length
# 1 <= n <= 105
# 1 <= nums[i] <= 109
# 0 <= removeQueries[i] < n
# removeQueries 中所有数字 互不相同 。
class UnionFind:
    def __init__(self, nums):
        n = len(nums)
        self.root = list(range(n))
        self.rank = [1] * n
        self.sums = nums.copy()

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return self.sums[x_root]
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.root[y_root] = x_root
        self.sums[x_root] += self.sums[y_root]
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1
        return self.sums[x_root]

    def get_sum(self, i):
        return self.sums[self.find(i)]


class Solution:
    def maximumSegmentSum(self, nums: [int], removeQueries: [int]) -> [int]:
        # 反向操作 + 并查集: 把正向的删除操作看成反向的添加操作，每次添加用并查集合并
        # 时间复杂度：O(n *  α(n)) n位数组长度，外层循环n次，内层每次可能存在合并操作，合并的采用了按秩合并，所以最终时间复杂度为O(n *  α(n))；其中α为阿克曼函数的反函数，α(n) 可以认为是一个很小的常数；
        # 空间复杂度：O(n)；
        union_find = UnionFind(nums)
        n = len(nums)
        res = [0] * n
        add_idx_set = set()
        for i in range(n - 1, 0, -1):  # 第一个被移除的数据，不用添加
            cur_add_idx = removeQueries[i]
            # 如果右边的值已经添加
            if (cur_add_idx + 1 in add_idx_set):
                union_find.union(cur_add_idx + 1, cur_add_idx)
            # 如果左边的值已经添加
            if (cur_add_idx - 1 in add_idx_set):
                union_find.union(cur_add_idx, cur_add_idx - 1)
            cur_sum = union_find.get_sum(cur_add_idx)
            # print(cur_sum)
            res[i - 1] = max(res[i], cur_sum)
            add_idx_set.add(cur_add_idx)
        return res
