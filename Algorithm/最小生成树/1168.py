# 1168. 水资源分配优化
# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。
#
# 对于每个房子 i，我们有两种可选的供水方案：
#
# 一种是直接在房子内建造水井，成本为 wells[i]；
# 另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，其中每个 pipes[i] = [house1, house2, cost] 代表用管道将 house1 和 house2 连接在一起的成本。当然，连接是双向的。
# 请你帮忙计算为所有房子都供水的最低总成本。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# 输出：3
# 解释：
# 上图展示了铺设管道连接房屋的成本。
# 最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。
# 示例 2：
#
# 输入：n = 2, wells = [1,1], pipes = [[1,2,1]]
# 输出：2
#
#
# 提示：
#
# 1 <= n <= 10000
# wells.length == n
# 0 <= wells[i] <= 10^5
# 1 <= pipes.length <= 10000
# 1 <= pipes[i][0], pipes[i][1] <= n
# 0 <= pipes[i][2] <= 10^5
# pipes[i][0] != pipes[i][1]

class Solution():

    def get_min_cost(self, wells, pipes):
        class UnionFindSet():
            def __init__(self, val, well_cost):
                self.val = val
                self.root = self
                self.k = 1
                self.well_cost = well_cost  # 在此房间建造水井的花费

            def find_root(self):
                if self.root == self:
                    return self
                root = self.root.find_root()
                self.root = root
                return root

        n = len(wells)
        # Kruskal 克鲁斯克尔算法 : 每次把最短的边加入生成图中，最终图中包含所有点时即为最小生成图
        pipes = sorted(pipes, key=lambda x: x[2])
        all_house_set = [UnionFindSet(i + 1, wells[i]) for i in range(n)]
        visited_house = set()
        res = 0
        for house1, house2, cost in pipes:
            root1 = all_house_set[house1 - 1].find_root()
            root2 = all_house_set[house2 - 1].find_root()
            if root1 == root2:
                continue
            if root1.well_cost < cost and root2.well_cost < cost:  # 建管道不划算
                if root1.val not in visited_house:
                    res += root1.well_cost
                if root2.val not in visited_house:
                    res += root2.well_cost
            else:  # 建管道划算
                res += cost
                if root1.well_cost <= root2.well_cost:
                    root2.root = root1  # root1的well_cost更小，把root1作为新的集合的root
                    if root1.val in visited_house and root2.val not in visited_house:
                        pass
                    elif root1.val in visited_house and root2.val in visited_house:
                        res -= root2.well_cost
                    elif root1.val not in visited_house and root2.val in visited_house:
                        res += (root1.well_cost - root2.well_cost)
                    else:
                        res += root1.well_cost
                else:
                    root1.root = root2  # root2的well_cost更小，把root2作为新的集合的root
                    if root1.val not in visited_house and root2.val in visited_house:
                        pass
                    elif root1.val in visited_house and root2.val in visited_house:
                        res -= root1.well_cost
                    elif root1.val in visited_house and root2.val not in visited_house:
                        res += (root2.well_cost - root1.well_cost)
                    else:
                        res += root2.well_cost
            visited_house.add(house1)
            visited_house.add(house2)

        return res


solu = Solution()
n = 3
wells = [1, 3]
pipes = [[1, 2, 5]]
print("res:", solu.get_min_cost(wells, pipes))
