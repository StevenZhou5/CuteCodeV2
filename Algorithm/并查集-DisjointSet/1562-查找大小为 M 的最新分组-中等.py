# 1562. 查找大小为 M 的最新分组
# 给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。
#
# 在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。
#
# 给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。
#
# 返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。
#
#
#
# 示例 1：
#
# 输入：arr = [3,5,1,2,4], m = 1
# 输出：4
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："00101"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："11101"，由 1 构成的组：["111", "1"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 存在长度为 1 的一组 1 的最后步骤是步骤 4 。
# 示例 2：
#
# 输入：arr = [3,1,5,4,2], m = 2
# 输出：-1
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："10100"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："10111"，由 1 构成的组：["1", "111"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 不管是哪一步骤都无法形成长度为 2 的一组 1 。
# 示例 3：
#
# 输入：arr = [1], m = 1
# 输出：1
# 示例 4：
#
# 输入：arr = [2,1], m = 2
# 输出：2
#
#
# 提示：
#
# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# arr 中的所有整数 互不相同
# 1 <= m <= arr.length

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.lens = [1] * n

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.root[y_root] = x_root
        self.lens[x_root] += self.lens[y_root]
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

    def get_len(self, i):
        return self.lens[self.find(i)]


class Solution:
    def findLatestStep(self, arr: [int], m: int) -> int:
        # 并查集：
        n = len(arr)
        union_find = UnionFind(n)
        visted_set = set()
        m_cnt = 0
        res_step = -1
        for step, idx in enumerate(arr):
            if idx in visted_set:
                if union_find.get_len(idx) == m:  # 如果把之前为m的合并了，m_cnt - 1
                    m_cnt -= 1
                union_find.union(idx, idx - 1)

            if idx - 2 in visted_set:
                if union_find.get_len(idx - 2) == m:  # 如果把之前为m的合并了，m_cnt - 1
                    m_cnt -= 1
                union_find.union(idx - 1, idx - 2)

            visted_set.add(idx - 1)
            if union_find.get_len(idx - 1) == m:  # 如果当前合并完为m个1，m_cnt + 1
                m_cnt += 1

            if m_cnt > 0:  # 只要m_cnt > 0 就需要更新step
                res_step = step + 1
        return res_step
