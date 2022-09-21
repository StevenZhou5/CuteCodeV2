# 547. 省份数量
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
#
#
#
# 示例 1：
#
#
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 示例 2：
#
#
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#
#
# 提示：
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class UnionFind:
    def __init__(self, isConnected):
        n = len(isConnected)
        self.root = list(range(n))
        self.rank = [1] * n
        self.count = n

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
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1
        self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: [[int]]) -> int:
        # 并查集：
        # 时间复杂度：O(n^2 * α(n)) 其中 n 是城市的数量。需要遍历矩阵n ^ 2; 每次遍历可能产生合并操作，合并操作中有查找和合并操作，如果不使用按秩合并最终时间复杂度为 O(n^2 *log n)； 如果使用按秩合并，最终时间复杂度为O(n^2 * α(n))，其中α为阿克曼函数的反函数，α(n) 可以认为是一个很小的常数
        # 空间复杂度：O(n)，其中 n 是城市的数量。需要使用数组 self.root 和 self.rank 记录每个城市所属的连通分量的祖先。

        union_find = UnionFind(isConnected)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, n):
                if not isConnected[i][j]:
                    continue
                union_find.union(i, j)

        return union_find.get_count()
