class UnionFind:
    def __init__(self, equations, values):
        self.root = {}
        self.rank = {}
        self.vals = {}
        n = len(equations)
        for i in range(n):
            a, b, val = equations[i][0], equations[i][1], values[i]
            if a not in self.root:
                self.root[a] = a
                self.rank[a] = 1
                self.vals[a] = 1

            if b not in self.root:
                self.root[b] = b
                self.rank[b] = 1
                self.vals[b] = 1

            self.union(b, a, val)

    def find(self, i):
        if i not in self.root:
            return None
        if self.root[i] != i:
            origin = self.vals[self.root[i]]
            self.root[i] = self.find(self.root[i])
            self.vals[i] *= origin  # 在进行路径压缩的时候，需要在更新root前先更新val

        return self.root[i]

    def union(self, x, y, val):
        # y = val * x
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        mid_val = self.get_val(x) / self.get_val(y)  # 默认是y合并到x, 注意这里一定要考虑 x 和 y 对应是原始root的倍数
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
            val = 1 / val  # 交换位置后，val要取倒数
            mid_val = self.get_val(y) / self.get_val(x)  # 交换位置，相当于是x合并到y上，此时mid_val要变为y
        self.root[y_root] = x_root
        self.vals[y_root] *= val * mid_val  # y_root 指向 a_root后，需要更新y_root的val
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

    def get_val(self, i):
        return self.vals[i]


class Solution:
    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
        # map + 递归
        # 时间复杂度：O(q * k), q 为queries的长度， k 为map的递归深度；
        # 空间复杂度：O(n + k), n 为equations的长度，k 为递归深度；
        # n = len(equations)
        # map_vals = {}
        # for i in range(n):
        #     key1, key2 = equations[i][0], equations[i][1]
        #     val1, val2 = values[i], 1 / values[i]
        #     key1_vals = map_vals.setdefault(key1, {})
        #     key1_vals[key2] = val1
        #     map_vals[key1] = key1_vals

        #     key2_vals = map_vals.setdefault(key2, {})
        #     key2_vals[key1] = val2
        #     map_vals[key2] = key2_vals
        # # print(map_vals)

        # visted_key = set() # 记录递归时已经访问过的节点
        # def dfs(key, sub_key):
        #     if key in visted_key:
        #         return -1.0
        #     if sub_key in map_vals[key]:
        #         return map_vals[key][sub_key]
        #     visted_key.add(key) # 没有直接找到时，需要下一层递归时再把key存上
        #     for item_key, item_val in map_vals[key].items():
        #         val = dfs(item_key, sub_key)
        #         if val != -1.0:
        #             val = item_val * val
        #             map_vals[key][sub_key] = val # 缓存新的键值，后续不用再重复
        #             return val

        #     return -1.0

        # res = []
        # for x1, x2 in queries:
        #     # print(x1, x2)
        #     if x1 not in map_vals or x2 not in map_vals:
        #         res.append(-1.0)
        #         continue
        #     if x1 == x2: # 剪枝
        #         res.append(1.0)
        #         continue
        #     visted_key.clear() # 需要清空访问结点
        #     res.append(dfs(x1, x2))
        # # print(map_vals)
        # return res

        # 并查集
        # 时间复杂度：O((N+Q)logA)，
        #   构建并查集 O(NlogA) ，这里 N 为输入方程 equations 的长度，每一次执行合并操作的时间复杂度是 O(logA)，这里 A 是 equations 里不同字符的个数；
        #   查询并查集 O(QlogA)，这里 Q 为查询数组 queries 的长度，每一次查询时执行「路径压缩」的时间复杂度是 O(logA)。
        # 空间复杂度：O(A)：创建字符与 id 的对应关系 hashMap 长度为 A，并查集底层使用的两个数组 parent 和 weight 存储每个变量的连通分量信息，parent 和 weight 的长度均为 A。
        union_find = UnionFind(equations, values)
        # print("before", union_find.root)
        # print("before", union_find.vals)
        res = []
        for a, b in queries:
            root_a = union_find.find(a)
            root_b = union_find.find(b)
            if not root_a or not root_b or root_a != root_b:
                res.append(-1.0)
                continue
            res.append(union_find.get_val(a) / union_find.get_val(b))
        # print(union_find.root)
        # print(union_find.vals)
        return res
