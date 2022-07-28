# 470. 用 Rand7() 实现 Rand10()
# pass
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
#
# 不要使用系统的 Math.random() 方法。
#
#
#
# 示例 1:
#
# 输入: 1
# 输出: [7]
# 示例 2:
#
# 输入: 2
# 输出: [8,4]
# 示例 3:
#
# 输入: 3
# 输出: [8,1,10]
#
#
# 提示:
#
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
#
#
# 进阶:
#
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
from random import randint


def Rnad7():
    return randint(1, 7)


class Solution():

    def rand10(self, n):
        # 1/2  * 1/5 = 1/10 策略
        if n < 1:
            return []

        res = []
        cnt = 0
        for i in range(n):
            a = Rnad7()
            cnt += 1
            # 如何减少生成1/2的概率时调用
            while a > 6:
                a = Rnad7()
                cnt += 1
            # while a > 2:  # 1/2 :这种方式每次只有2/7的概率能满足要求，效率比较第
            #     a = randint(1, 7)
            #     cnt += 1
            b = Rnad7()
            cnt += 1
            while b > 5:  # 1/5
                b = Rnad7()
                cnt += 1
            res.append(b if a & 1 == 1 else b + 5)
            # res.append(randint(1, 10))
        print("平均每次调用rand7的次数为:", cnt / n)
        from collections import Counter
        count_res = Counter(res)
        print("counter res:", sorted(count_res.items(), key=lambda x: x[0]))
        return res

    def rand10_2(self, n):
        # 7行7列只取前面40个数，用这40个数与10的余数计算结果
        cnt = 0
        res = []
        for _ in range(n):
            idx = 50
            while idx > 40:
                row = Rnad7()
                col = Rnad7()
                idx = (row - 1) * 7 + col
                cnt += 2
            cur_val = idx % 10
            res.append(cur_val if cur_val > 0 else 10)
        print("cnt:", cnt / n)
        from collections import Counter
        count_res = Counter(res)
        print("counter res:", sorted(count_res.items(), key=lambda x: x[0]))
        return res


solu = Solution()
solu.rand10_2(10000)
solu.rand10(10000)
# print("res:", solu.rand10(1000000))
