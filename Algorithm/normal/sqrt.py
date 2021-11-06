class Solution(object):

    def __init__(self):
        pass

    def sqrt(self, num, precision=1e-9):
        if num == 0 or num == 1:
            return num
        left, right = 0, num
        mid = left + (right - left) / 2
        cur_val = mid * mid
        while abs(num - cur_val) > precision:
            print("cur_mid:", mid)
            if cur_val < num:
                left = mid
            else:
                right = mid
            mid = left + (right - left) / 2
            cur_val = mid * mid

        return mid


solu = Solution()
num = 10
print("res:", solu.sqrt(num, 1e-14))
import math

print("sys_res:", math.sqrt(num))
