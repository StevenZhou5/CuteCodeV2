# 1135. 最低成本联通所有城市
# 想象一下你是个城市基建规划者，地图上有 N 座城市，它们按以 1 到 N 的次序编号。
#
# 给你一些可连接的选项 conections，其中每个选项 conections[i] = [city1, city2, cost] 表示将城市 city1 和城市 city2 连接所要的成本。（连接是双向的，也就是说城市 city1 和城市 city2 相连也同样意味着城市 city2 和城市 city1 相连）。
#
# 返回使得每对城市间都存在将它们连接在一起的连通路径（可能长度为 1 的）最小成本。该最小成本应该是所用全部连接代价的综合。如果根据已知条件无法完成该项任务，则请你返回 -1。
#
# 
#
# 示例 1：
#
#
#
# 输入：N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]
# 输出：6
# 解释：
# 选出任意 2 条边都可以连接所有城市，我们从中选取成本最小的 2 条。
# 示例 2：
#
#
#
# 输入：N = 4, conections = [[1,2,3],[3,4,4]]
# 输出：-1
# 解释：
# 即使连通所有的边，也无法连接所有城市。
#
#
# 提示：
#
# 1 <= N <= 10000
# 1 <= conections.length <= 10000
# 1 <= conections[i][0], conections[i][1] <= N
# 0 <= conections[i][2] <= 10^5
# conections[i][0] != conections[i][1]

class Solution():

    def get_min_cost(self, N, conections):
        class UnionFindSet():
            def __init__(self, val):
                self.val = val
                self.k = 1
                self.root = self

            def find_root(self):
                if self.root == self:  #
                    return self
                root = self.root.find_root()
                self.root = root # 重新赋值一下root，加速后续的查找
                return root

        # Kruskal 克鲁斯克尔算法 : 每次把最短的边加入生成图中，最终图中包含所有点时即为最小生成图
        conections = sorted(conections, key=lambda x: x[2])

        print(conections)
        visited_city = set()
        root_set = [UnionFindSet(i + 1) for i in range(N)]
        res = 0
        for city1, city2, distance in conections:
            city1_root = root_set[city1 - 1].find_root()
            city2_root = root_set[city2 - 1].find_root()
            if city1_root != city2_root:  # 不在同一个集合时，需要添加此边
                res += distance
                if city1_root.k > city2_root.k:
                    city2_root.root = city1_root
                elif city1_root.k < city2_root.k:
                    city1_root.root = city2_root
                else:
                    city2_root.root = city1_root
                    city1_root.k = city1_root.k + 1

                visited_city.add(city1)
                visited_city.add(city2)
        # 所有结点是否都访问了，没有返回-1
        if len(visited_city) < N:
            return -1
        # 确定集合是否唯一，唯一的话只有一个root
        only_root = root_set.pop().find_root()
        while root_set:
            if only_root != root_set.pop().find_root():
                return -1
        return res


solu = Solution()
N = 3
conections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
print("res:", solu.get_min_cost(N, conections))
