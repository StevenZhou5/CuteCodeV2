# 638. 大礼包
# 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
#
# 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。
#
# 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。
#
# 返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。
#
#
#
# 示例 1：
#
# 输入：price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
# 输出：14
# 解释：有 A 和 B 两种物品，价格分别为 ¥2 和 ¥5 。
# 大礼包 1 ，你可以以 ¥5 的价格购买 3A 和 0B 。
# 大礼包 2 ，你可以以 ¥10 的价格购买 1A 和 2B 。
# 需要购买 3 个 A 和 2 个 B ， 所以付 ¥10 购买 1A 和 2B（大礼包 2），以及 ¥4 购买 2A 。
# 示例 2：
#
# 输入：price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
# 输出：11
# 解释：A ，B ，C 的价格分别为 ¥2 ，¥3 ，¥4 。
# 可以用 ¥4 购买 1A 和 1B ，也可以用 ¥9 购买 2A ，2B 和 1C 。
# 需要买 1A ，2B 和 1C ，所以付 ¥4 买 1A 和 1B（大礼包 1），以及 ¥3 购买 1B ， ¥4 购买 1C 。
# 不可以购买超出待购清单的物品，尽管购买大礼包 2 更加便宜。
#
#
# 提示：
#
# n == price.length
# n == needs.length
# 1 <= n <= 6
# 0 <= price[i] <= 10
# 0 <= needs[i] <= 10
# 1 <= special.length <= 100
# special[i].length == n + 1
# 0 <= special[i][j] <= 50

class Solution():
    def min_cost_dp_sc(self, price, special, needs):
        if not price:
            return 0
        n = len(needs)
        # 状态定义 dp[(c1,c2...cn)] 代表第一件物品选c1个，第二物品选c2个......第n个物品选cn个 所需要的最少的钱
        # 使用二进制进行状态表示，其中1 <= n <= 6 , 0 <= needs[i] <= 10 ; 所以我们用4个二进制为表示一个物品的数量，最多需要32位
        # 0010 0000 0001 1000 1010 1001 代表第一件物品选1001 = 9件；第二件物品选1010=10件；第三件物品选1000=8件；第四件物品0001=1选一件；第五件物品0000=0选0件；第六件物品0010=2选两件；
        dp = {}
        final_state = 0
        for i in range(n):
            final_state += needs[i] << (4 * i)
        print(final_state)

        def recursion(cur_state):
            # 递归终止条件:不需要买任何物品了
            if cur_state == 0:
                dp[cur_state] = 0
                return 0
            if cur_state in dp:
                return dp[cur_state]

            cur_min_cost = float('inf')  # 依次选每一个礼包或者每一个商品，计算满足的最小消费
            for spe in special:  # 一个礼包一个礼包的选
                tmp_state = cur_state
                new_state = 0
                for i in range(n):
                    # 计算商品i还需要的数目
                    tmp_state, need_i_cnt = tmp_state >> 4, tmp_state - ((tmp_state >> 4) << 4)
                    # print("tmp_state:%d; need_i_cnt:%d; " % (tmp_state, need_i_cnt))
                    if spe[i] > need_i_cnt:  # 选了此礼包会使某个物品超过需要的数目，那么不能选择此礼包
                        break
                    new_state += (need_i_cnt - spe[i]) << (i * 4)
                else:
                    # 循环正常执行完成，选择当前礼包
                    cur_min_cost = min(recursion(new_state) + spe[-1], cur_min_cost)  # 更新最小花费:剩余的最小花费 + 当前礼包的钱
                continue  # 如果内存循环break，完成循环continue

            for i in range(n):  # 一个商品一个商品的选
                tmp_state = cur_state >> (i * 4)
                need_i_cnt = tmp_state - ((tmp_state >> 4) << 4)
                print("第 %d 个商品的 need_i_cnt: %d" % (i, need_i_cnt))
                if need_i_cnt == 0:
                    continue
                new_state = cur_state - (1 << (i * 4))  # 第i个商品需要的数量-1
                cur_min_cost = min(cur_min_cost, recursion(new_state) + price[i])  # 更新最小花费:
            dp[cur_state] = cur_min_cost
            return cur_min_cost

        res = recursion(final_state)
        print("dp:", dp)
        return res


solu = Solution()
price, special, needs = [2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]
# price, special, needs = [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]
print("res:", solu.min_cost_dp_sc(price, special, needs))
