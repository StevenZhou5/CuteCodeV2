class Solution():
    def get_min_step(self, s1, s2):
        if not s1 and not s2:
            return 0
        m, n = len(s1), len(s2)
        if not m or not n:
            return max(m, n)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i - 1][j] + 1
                left = dp[i][j - 1] + 1
                up_left = dp[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                # print((i, j), "up:", up, "; left:", left, "; up_left:", up_left)
                dp[i][j] = min(up, left, up_left)
        print(dp)
        return dp[m][n]


s1 = "ss"
s2 = "aa"
solu = Solution()
print("%s 与 %s 的距离为：%d" % (s1, s2, solu.get_min_step(s1, s2)))
