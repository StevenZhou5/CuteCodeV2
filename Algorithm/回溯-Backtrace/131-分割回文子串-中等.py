# 131. 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
# 提示：
#
# 1 <= s.length <= 16
# s 仅由小写英文字母组成
from functools import lru_cache
# from cachetools.func import lru_cache


class Solution:
    def partition(self, s: str) -> [[str]]:
        # 递归 + 回溯 + 记忆化
        # 时间复杂度：O()
        self.n = len(s)
        self.res = []
        self.cur_res = []

        # self.state_map = {} 手动维护，或者使用lru_cache

        @lru_cache(None)  # 使用记忆化
        def is_valid(i, j):
            # if (i,j) in self.state_map:
            #     return self.state_map[(i,j)]
            # print(s[i: j + 1])
            # 判断 i 到 j 的子串是否为回文子串,中心扩散法
            state = True
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    state = False
                    break
            # self.state_map[(i,j)] = state
            return state

        def recursion(start):
            # 递归终止
            if start >= self.n:
                self.res.append(self.cur_res.copy())
                return

            for i in range(start, self.n):
                # print(start, i)
                if is_valid(start, i):
                    self.cur_res.append(s[start:i + 1])
                    recursion(i + 1)
                    self.cur_res.pop()  # 回溯

        recursion(0)
        return self.res
