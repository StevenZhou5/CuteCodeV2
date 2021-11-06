class Solution(object):

    def __init__(self):
        pass

    def strStr(self, stra, strb):
        if len(stra) < len(strb):
            return -1
        if not strb:
            return 0

        b_len = len(strb)
        res = -1
        for i in range(len(stra)):
            if stra[i:i + b_len] == strb:
                res = i
                break

        return res


solu = Solution()
a = "sddda"
b = "da"
print("res:", solu.strStr(a, b))
print("index:", a.index(b))
