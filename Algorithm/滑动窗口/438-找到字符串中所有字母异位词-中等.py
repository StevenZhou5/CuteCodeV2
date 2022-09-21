# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#
#
# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
# 提示:
#
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        # 滑动窗口
        # 时间复杂度：O(m + n)，一次遍历p,统计计数，时间复杂度O(n);一次遍历s，最多左右指针各移动一次 时间复杂度O(m),
        # 空间复杂度：O(Σ) 存字符串p种不同字母的个数，Σ最大为26
        m, n = len(s), len(p)
        counter_p = collections.Counter(p)
        distance = n  # 用类似汉明距离的方式来记录两个字符串的，差距，只有当字符串距离为0时才代表是异位词 及相同字母的个数相同
        counter_sub_s = collections.defaultdict(int)

        l, r = 0, 0
        res = []
        # print(counter_p)
        while r < m:
            # print(l, r, counter_sub_s, distance)
            if s[r] in counter_p:
                counter_sub_s[s[r]] += 1
                if counter_sub_s[s[r]] <= counter_p[s[r]]:  # 增加了一个有效字符，距离-1
                    distance -= 1
            r += 1

            if r > n:  # 因为上面r先加了1，所以要 r 要大于n
                if s[l] in counter_p:
                    counter_sub_s[s[l]] -= 1
                    if counter_sub_s[s[l]] < counter_p[s[l]]:  # 减去了一个有效字符，距离 +1
                        distance += 1
                l += 1
            # print("end:", l, r, counter_sub_s, distance)
            if distance == 0:
                res.append(l)
        return res
