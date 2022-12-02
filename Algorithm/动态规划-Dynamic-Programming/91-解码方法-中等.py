# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。
#
#
#
# 示例 1：
#
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
#
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
#
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#
#
# 提示：
#
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。

class Solution:
    def numDecodings(self, s: str) -> int:
        # 递归 + 回溯 : 会超时
        # valid_set = set()
        # for i in range(1, 27):
        #     valid_set.add(str(i))
        # # print(valid_set)

        # self.n = len(s)
        # self.res = 0
        # def recursion(start_idx):
        #     if start_idx >= self.n:
        #         self.res += 1
        #         return

        #     if s[start_idx] in valid_set:
        #         recursion(start_idx + 1)
        #     if start_idx < self.n -1 and s[start_idx: start_idx + 2] in valid_set:
        #         recursion(start_idx + 2)

        # recursion(0)
        # return self.res

        # 动态规划
        # 时间复杂： O(n) ,遍历一次
        # 空间复杂度： O(1)， 只缓存的pre和pre_pre
        valid_set = set()
        for i in range(1, 27):
            valid_set.add(str(i))
        # print(valid_set)

        # step1 状态定义
        dp_pre_pre = 1  # dp[i] 代表以第i个字符为结尾前面所有字符总共有多少种解码方法
        dp_pre = 1 if s[0] in valid_set else 0
        # print(dp_pre_pre, dp_pre)
        n = len(s)
        for i in range(1, n):
            # step2： 状态转移
            cur_val = 0
            if s[i] in valid_set:
                cur_val += dp_pre
            if s[i - 1: i + 1] in valid_set:
                cur_val += dp_pre_pre
                # print(i, s[i], s[i-1: i + 1], cur_val)
            dp_pre_pre, dp_pre = dp_pre, cur_val

        return dp_pre
