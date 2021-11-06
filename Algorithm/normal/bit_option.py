class Solution():
    def __init__(self):
        pass

    def how_many_one(self, num):
        cnt = 0
        while num != 0:
            cnt += 1
            num &= num - 1
        return cnt

    def is_power_2_n(self, num):
        return num != 0 and not num & num - 1

    def how_many_one_all_n(self, n):
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i & i - 1] + 1
        return res


from random import randint

solu = Solution()
num = randint(0, 100)
print("num", num)
print("how_many_one:", solu.how_many_one(num))
print("is_power_2_n:", solu.is_power_2_n(num))
print("how_many_one_all_n", solu.how_many_one_all_n(num))
