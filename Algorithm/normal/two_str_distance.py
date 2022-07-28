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
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == j == 0:
                    continue
                up = 1 + dp[i - 1][j] if i > 0 else float("inf")
                left = 1 + dp[i][j - 1] if j > 0 else float('inf')
                up_left = (dp[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)) if i > 0 and j > 0 else float('inf')
                # print((i, j), "up:", up, "; left:", left, "; up_left:", up_left)
                dp[i][j] = min(up, left, up_left)
        print(dp)
        return dp[m][n]


s1 = "ssa"
s2 = "afwddf"
solu = Solution()
print("%s 与 %s 的距离为：%d" % (s1, s2, solu.get_min_step(s1, s2)))
