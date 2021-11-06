class BitOperationNPower(object):
    def __init__(self):
        pass

    def power(self, x, n):
        res = 1

        while n > 0:
            # print(n)
            if n & 1:  # 如果n为奇数，需要乘上自己
                res *= x
            x *= x
            n >>= 1

        return res


bp = BitOperationNPower()
print(bp.power(2, 10))

