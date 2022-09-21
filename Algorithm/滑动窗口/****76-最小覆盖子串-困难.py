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
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口 + hash计数 + distince
        # 时间复杂度：O(len(s) + len(t)), 只遍历了一次s, 且用distance判断是否完全匹配的时间复杂度为O(1)
        # 空间复杂度：O(len(t)) 只记录了t种出现字符的频数数组
        distince = len(t)  # 用distance来表示s的子串和t的距离，distance == 0 时说明s的子串包含所有的t种的子串；distance最大值为len(t)
        counter_t = collections.Counter(t)  # 用来记录t的字符频数
        counter_s = {}  # 用来动态的记录 s 的子串的字符频数

        l, r = 0, 0  # [l,r),左闭右开，用来记录滑动窗口的区间，初始相当于没有字符
        n = len(s)  # s 字符串的长度
        res_l, res_len = 0, n + 1  # 用来记录最终结果，res_len 初始比s的长度大即可-这样可以在最后用于判断是否找到了子串
        while r < n:
            # 右边界移动
            if s[r] not in counter_t:  # 如果字符不是t种的目标字符，不用关心
                r += 1
                continue

            counter_s[s[r]] = counter_s.get(s[r], 0) + 1
            if counter_s[s[r]] <= counter_t[s[r]]:  # 只有counter_s[s[r]] 的个数<= counter_t[s[r]] 才可以在添加一个字符的时候减少距离
                distince -= 1
            r += 1

            # 滑动窗口在所有字符都匹配的时候移动左边界
            while distince == 0:
                if s[l] not in counter_t:
                    l += 1
                    continue
                # print(l, r)
                # 在窗口左移的时候会产生最小覆盖子串，所以在这个时候进行判断
                if (r - l) < res_len:
                    # print(l, r)
                    res_l, res_len = l, r - l

                counter_s[s[l]] = counter_s.get(s[l], 0) - 1
                if counter_s[s[l]] < counter_t[s[l]]:  # s[l] 的在窗口中的字符频数已经不足时增加distance
                    distince += 1
                l += 1
        # print(res_l, res_len)
        return s[res_l: res_l + res_len] if res_len <= n else ""
