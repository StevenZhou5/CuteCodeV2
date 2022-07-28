# 332. 重新安排行程
# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
#
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
#
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
# 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
#
#
#
# 示例 1：
#
#
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
# 示例 2：
#
#
# 输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
#
#
# 提示：
#
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi 和 toi 由大写英文字母组成
# fromi != toi

class Solution:
    def findItinerary(self, tickets):
        from_to_map = {}
        ticket_cnt = len(tickets)
        for fromi, toi in tickets:
            cur_to_list = from_to_map.setdefault(fromi, [])
            cur_to_list.append(toi)
        print(from_to_map)

        res = []

        def dfs(visted, cur, cur_res):
            # print(all_target_set, visted)
            if len(visted) == ticket_cnt:  # 所有票都用完了
                res.append(cur_res.copy())  # 存储结果
                return

            for next in from_to_map.get(cur):
                if (cur, next) in visted:
                    continue
                # 记录
                visted.add((cur, next))
                cur_res.append(next)

                # 递归
                dfs(visted, next, cur_res)

                # 回溯
                cur_res.pop()
                visted.remove((cur, next))

        dfs(set(), "JFK", ["JFK"])
        print("all_res:", res)
        return min(res)


solu = Solution()
# tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print("tickets:", tickets)
print("res:", solu.findItinerary(tickets))
