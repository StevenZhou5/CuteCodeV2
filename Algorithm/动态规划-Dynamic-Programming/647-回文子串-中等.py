# 647. 回文子串
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
#
# 回文字符串 是正着读和倒过来读一样的字符串。
#
# 子字符串 是字符串中的由连续字符组成的一个序列。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#
#
# 示例 1：
#
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：
#
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 由小写英文字母组成
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划
        # 时间复杂度：O(n ^ 2)
        # 空间复杂度：O(n ^ 2)
        # n = len(s)
        # step1: 状态定义
        # dp = [[True if i == j else False for j in range(n)]  for i in range(n)] # dp[i][j] 从第i个字符到第j个字符是否是回文子串
        # # print(dp)
        # self.res = n
        # for col in range(1,n):
        #     for row in range(col - 1, -1, -1):
        #         # print(row, col)
        #         dp[row][col] = s[row] == s[col] and (dp[row + 1][col - 1] if col > row + 1 else True)
        #         if dp[row][col]:
        #             self.res += 1
        # # print(dp)
        # return self.res

        # Manacher 算法
        # 时间复杂度：O(n)。即 Manacher 算法的时间复杂度，由于最大回文右端点 r_m
        # 只会增加而不会减少，故中心拓展进行的次数最多为 O(n)，此外我们只会遍历字符串一次，故总复杂度为 O(n)。
        # 空间复杂度：O(n) 存储每个位置的最大半径。
        n = len(s)
        new_s = "$"
        for i in range(n):
            new_s += "#" + s[i]
        new_s += "#!"
        # print(new_s)

        max_i = 0
        max_r = 0
        new_n = len(new_s)
        dp = [1] * new_n  # 存储每个位置最大半径
        res = 0
        for i in range(new_n):
            # 初始化当前半径
            if i < max_r:
                left_i = 2 * max_i - i
                dp[i] = min(max_r - i, dp[left_i])
            l, r = i - dp[i] + 1, i + dp[i] - 1
            while l - 1 >= 0 and r + 1 < new_n and new_s[l - 1] == new_s[r + 1]:
                dp[i] += 1
                l, r = i - dp[i] + 1, i + dp[i] - 1
            res += dp[i] >> 1  # 半径的一半是真正有效的回文子串个数
            if dp[i] > max_r - max_i:
                max_i, max_r = i, i + dp[i] - 1
        # print(dp)
        return res

        # 中心扩散
        # 时间复杂度 O(n ^ 2)
        # 空间复杂度 O(1) , 采用循环的方式，没有额外的存储空间
        n = len(s)

        self.res = 1

        def expand_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1

        for i in range(1, n):
            expand_center(i, i)
            expand_center(i - 1, i)
        return self.res
