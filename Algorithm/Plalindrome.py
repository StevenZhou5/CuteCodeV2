class Plalindrome(object):
    def __init__(self):
        super(Plalindrome, self).__init__()

    def find_max_substr_by_dynamic_programming(self, str):
        print("######### 动态规划法寻找最长回文子串 ###########", str)
        if not str:
            return None
        len_s = len(str)
        if len(str) == 1:
            return str

        P = [[False] * len_s for _ in range(len_s)]
        for i in range(len_s):
            P[i][i] = True

        print(P)
        max_len = 1
        start_idx = 0
        for j in range(1, len_s):
            for i in range(j - 1, -1, -1):
                if str[i] == str[j]:
                    if j == i + 1:
                        P[i][j] = True
                    else:
                        P[i][j] = P[i + 1][j - 1]
                    if P[i][j] and (j - i + 1) > max_len:
                        start_idx = i
                        max_len = (j - i + 1)
                else:
                    P[i][j] = False
        print(P)

        return str[start_idx: start_idx + max_len]

    def find_max_substr_by_center_expand(self, str):
        print("########## 中心扩散法寻找最长回文子串  ###########", str)
        if not str:
            return None
        if len(str) == 1:
            return str

        def expand(str, center_idx1, center_idx2):
            # print("%s expand form: %d , %d" % (str, center_idx1, center_idx2))
            max_len = 0
            while center_idx1 >= 0 and center_idx2 < len(str):
                if str[center_idx1] == str[center_idx2]:
                    max_len = center_idx2 - center_idx1 + 1
                    center_idx1 -= 1
                    center_idx2 += 1
                else:
                    return max_len, center_idx1 + 1
            return max_len, center_idx1 + 1

        max_len = 1
        max_idx = 0
        for i in range(0, len(str) - 2):
            max_len1, max_idx1 = expand(str, i, i)
            max_len2, max_idx2 = expand(str, i, i + 1)
            if max_len1 > max_len:
                max_len, max_idx = max_len1, max_idx1
            if max_len2 > max_len:
                max_len, max_idx = max_len2, max_idx2
        print("max_len:%d; max_idx:%d" % (max_len, max_idx))
        return str[max_idx:(max_idx + max_len)]

# p = Plalindrome()
# str = "acbbccbbcsddffffggs"
# print(p.find_max_substr_by_dynamic_programming(str))

# p = Plalindrome()
# str = "acbbccbbcsddffffggs"
# print("res:", p.find_max_substr_by_center_expand(str))
