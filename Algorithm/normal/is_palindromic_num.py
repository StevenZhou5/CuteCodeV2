class Solution(object):
    def __init__(self):
        pass

    def is_palindromic_num(self, num):
        if num < 0 or (num != 0 and num % 10 == 0):
            return False

        last_half = 0
        while num > last_half:
            last_half, num = last_half * 10 + num % 10, num // 10

        return last_half == num or num == last_half // 10  # 长度为偶数两个值相等，长度为奇数last_half去除最后一位


solu = Solution()
num = 10
print("num is palindromic num:", solu.is_palindromic_num(num))
