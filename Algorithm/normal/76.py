# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
# 提示：
#
# 1 <= s.length, t.length <= 105
# s 和 t 由英文字母组成
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

class Solution():

    def get_t_from_s_with_slidding_window(self, s, t):
        if not s or not t:
            return ""

        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        print("counter_s:", counter_s, "; counter_t:", counter_t)

        for key in counter_t:
            if counter_s[key] < counter_t[key]:  # 如果任何一个字符的数不够则return
                return ""

        shrink_idx = 0
        expand_idx = 0
        res = s
        window_counter = Counter()

        def is_valid():
            for key in counter_t:
                if window_counter[key] < counter_t[key]:
                    return False
            return True

        while expand_idx < len(s):
            key = s[expand_idx]
            if key in counter_t:
                window_counter[key] = window_counter[key] + 1
            # print(window_counter)

            while is_valid():
                res = res if len(res) <= (expand_idx - shrink_idx + 1) else s[shrink_idx:(expand_idx + 1)]
                key = s[shrink_idx]
                if key in counter_t:
                    window_counter[key] -= 1
                shrink_idx += 1
            expand_idx += 1
        return res


s = "asdsdeeees"
t = "eeesd"
solu = Solution()
print("res:", solu.get_t_from_s_with_slidding_window(s, t))
