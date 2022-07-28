# 1192. 查找集群内的「关键连接」
# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。
#
# 它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。
#
# 从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
#
# 「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
#
# 请你以任意顺序返回该集群内的所有 「关键连接」。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。
#
#
# 提示：
#
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# 不存在重复的连接

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if not connections:
            return []

        # dfs, id 合并 id, 动态判断
        def make_node_map():
            res_map = {}
            for node1, node2 in connections:
                node1_list = res_map.setdefault(node1, [])
                node1_list.append(node2)

                node2_list = res_map.setdefault(node2, [])
                node2_list.append(node1)
            return res_map

        node_map = make_node_map()  # 所有结点和相邻结点的map
        id_list = [-1] * len(node_map)  # 存放每个结点id的list
        res = []  # 最终的关键连接结果

        # print(node_map)

        def dfs(cur_node, node_id, parent_node):
            id_list[cur_node] = node_id  # 先把当前结点的id赋值为父节点高速的id

            for nei_node in node_map[cur_node]:
                if nei_node == parent_node:  # 相邻结点是父节点那么直接跳过
                    continue
                elif id_list[nei_node] == -1:  # 相邻结点为访问过:更新当前结点id为dfs后的nei结点id和当前结点id的最小值
                    id_list[cur_node] = min(id_list[cur_node], dfs(nei_node, node_id + 1,
                                                                   cur_node))  # 注意，这里一定要用node_id +1,不能用id_list[cur_node] + 1 ,因为id_list[cur_node]会在循环的时候被该表
                else:  # 相邻结点被访问过,更新当前结点id值为两个结点id中更小的那个
                    id_list[cur_node] = min(id_list[cur_node], id_list[nei_node])

            if cur_node != 0 and node_id == id_list[cur_node]:
                # 如果当前结点不是起始的根结点，并且父节点高速的id和最终dfs结束后的id一致，那么说明父节点和当前结点所构成的边不在环内(如果父节点和当前结点在同一个环的话node_id 一定大于id_list[cur_node])，即为关键连接
                res.append([parent_node, cur_node])

            return id_list[cur_node]  # dfs 要把当前结点的最终id作为返回值

        dfs(0, 0, -1)

        return res
