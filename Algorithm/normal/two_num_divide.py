class Solution(object):

    def __init__(self):
        pass

    def divide(self, dividend, divisor):
        res = 0
        is_positive = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False

        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            cur_divisor = divisor
            cur_res = 1
            while dividend >= cur_divisor:  # 至少会执行一次
                cur_divisor <<= 1
                cur_res <<= 1
            cur_divisor >>= 1
            cur_res >>= 1
            print("cur_divisor:%d; cur_res:%d; dividend:%d" % (cur_divisor, cur_res, dividend))
            dividend -= cur_divisor
            res += cur_res
        return res if is_positive else -(res + (0 if dividend == 0 else 1))


solu = Solution()

print("res:", solu.divide(-501, 4))
