# 1584. 连接所有点的最小费用
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
#
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
#
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
#
#
#
# 示例 1：
#
#
#
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
#
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
# 示例 2：
#
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
# 示例 3：
#
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
# 示例 4：
#
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
# 示例 5：
#
# 输入：points = [[0,0]]
# 输出：0
#
#
# 提示：
#
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# 所有点 (xi, yi) 两两不同。

class Solution():

    def get_min_val(self, points):
        # Kruskal 克鲁斯克尔算法
        all_items = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                all_items.append(((i, j), abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        all_items = sorted(all_items, key=lambda x: x[1], )
        print(all_items)
        visited_set = set()
        res = 0
        # Kruskal 克鲁斯克尔算法 : 每次把最短的边加入生成图中，最终图中包含所有点时即为最小生成图
        for (point1, point2), distance in all_items:
            # print(point1, point2, distance)
            if len(visited_set) == n:  # 所有结点都有了，返回
                break
            if point1 not in visited_set or point2 not in visited_set:
                visited_set.add(point1)
                visited_set.add(point2)
                res += distance

        return res


# points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
solu = Solution()
print("res:", solu.get_min_val(points))
