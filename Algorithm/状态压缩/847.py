# 847. 访问所有节点的最短路径
# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
#
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
#
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
#
#
#
# 示例 1：
#
#
# 输入：graph = [[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一种可能的路径为 [1,0,2,0,3]
# 示例 2：
#
#
#
# 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一种可能的路径为 [0,1,4,2,3]
#
#
# 提示：
#
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] 不包含 i
# 如果 graph[a] 包含 b ，那么 graph[b] 也包含 a
# 输入的图总是连通图

class Solution():

    def get_min_path_dp_sc_dfs(self, graph):
        # 状态定义 dp[(state,cur_idx))] 代表 当前状态下，最后停留在cur_idx的最小路径
        # state 用二进制表示，，假设有4个点 ， (1001 , 0) 代表走过第一个点和第四个点的最后停留在位置0点的状态
        dp = {}
        n = len(graph)
        final_state = (1 << n) - 1
        self.res = float('inf')
        print("final_state:", final_state)

        def recursion(cur_state, cur_idx, cur_path_len):
            # print(cur_state, cur_idx, cur_path_len)
            # 递归终止条件
            if cur_state == final_state:
                dp[(cur_state, cur_idx)] = cur_path_len
                self.res = min(cur_path_len, self.res)
                return

            if (cur_state, cur_idx) in dp and cur_path_len >= dp[(cur_state, cur_idx)]:  # 如果已经在了，并且新的怕path没有更小
                return
            # 不存在 或者 新的path 更小
            dp[(cur_state, cur_idx)] = cur_path_len

            for next_idx in graph[cur_idx]:
                next_idx_state = 1 << next_idx
                new_cur_state = cur_state | next_idx_state  # 可以走到已经访问过的结点，因为此时的cur_idx不同了
                recursion(new_cur_state, next_idx, cur_path_len + 1)
            return

        # recursion(3, 0, 1)
        for idx in range(n):
            recursion(1 << idx, idx, 0)
        print(dp)
        return self.res


solu = Solution()
# graph = [[1, 2, 3], [0], [0], [0]]
graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print("res:", solu.get_min_path_dp_sc_dfs(graph))
