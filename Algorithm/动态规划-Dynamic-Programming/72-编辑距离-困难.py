# 72. 编辑距离
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
# 提示：
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成

class Solution():
    def min_distance(self, word1, word2):
        if not word1 and not word2:
            return 0
        len_1 = len(word1)
        len_2 = len(word2)
        # 状态定义：word1的前i个字符变成word2的前j个字符所需要的最小编辑距离
        # 初始为word1从"" 变为 word2 依次所需要的编辑距离(即为j),注意一定要把""字符也算上
        dp = [j for j in range(len_2 + 1)]  # 只存上一行dp数据，优化空间复杂度
        print("第 %s 行的dp值为:" % (" "), dp)
        for i in range(1, len_1 + 1):
            pre_up_left = dp[0]
            dp[0] = dp[0] + 1  # 由于第0列只能有上面转移过来，所以更新当前行的第0列
            for j in range(1, len_2 + 1):  # 第0列已经初始话了
                # 状态转移：
                # 1： 从 [i-1][j] 转移到[i][j]:  dp[i][j] = dp[i-1][j] + 1; word1的前i-1个变成word2的前j个后还需要删除word1[i]
                up = dp[j] + 1
                # 2: 从[i][j-1] 转移到[i][j]: dp[i][j] = dp[i][j-1] + 1; word1的前i个变成word2的前j-1个后还需要添加一个word2[j]
                left = dp[j - 1] + 1
                # 3: 从[i-1][j-1] 转移到[i][j]: dp[i][j] = dp[i-1][j-1] + 0 if word1[i] == word2[j] else 1;
                # word1的前i-1个变成word2的前j-1个后，如果word[i] == word[j] 那么不需要其他额外操作，否则还需要一步将word[i] 变为 word[j]
                up_left = pre_up_left + (0 if word1[i - 1] == word2[j - 1] else 1)  # 注意idx都要-1

                pre_up_left = dp[j]  # 更新up_left,因为它的位置马上要被当前值覆盖了
                dp[j] = min(up, left, up_left)
            print("第 %s 行的dp值为:" % (word1[i - 1]), dp)
        return dp[-1]

    def min_distance_v2(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[i + j if not i or not j else float('inf') for j in range(n + 1)] for i in range(m + 1)]
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + (1 if s[i - 1] != p[j - 1] else 0)  # 改
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)  # 删
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)  # 增
        print(dp)
        return dp[m][n]


solu = Solution()
# word1 = "a"
# word2 = "ba"
# word1 = "horse"
# word2 = "ros"
word1 = "intention"
word2 = "execution"
print("word1:%s; word2:%s;" % (word1, word2))
print("res:", solu.min_distance(word1, word2))
print("res2:", solu.min_distance_v2(word1, word2))
