# 28. 找出字符串中第一个匹配项的下标
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#
#
#
# 示例 1：
#
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：
#
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#
#
# 提示：
#
# 1 <= haystack.length, needle.length <= 104
# haystack 和 needle 仅由小写英文字符组成

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 滚动hash
        # 时间复杂度 ：O(m + n), 如果mod取值合理，没有冲突或者冲突较少的情况下 haystack 遍历一次O(m), needle 最多遍历k次 k * O(n)
        # 空间复杂度 ：O(1)
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        base = 30  # 核心参数1
        mod = 999983  # 核心参数2
        tar_hash = 0
        ord_a = ord('a')
        #  step 1 ： 计算目标 hash值
        for c in needle:
            tar_hash = (tar_hash * base) % mod + ((ord(c) - ord_a) * base) % mod
            # print(tar_hash)

        #  step2 : 根据目标字符串长度n计算n_base
        n_base = 1
        for _ in range(n):
            n_base = (n_base * base) % mod
            # print(n_base)

        #  step3： 滚动计算子串hash值
        cur_hash = 0
        for l in range(m - n + 1):
            if l == 0:
                for i in range(n):
                    cur_hash = (cur_hash * base) % mod + ((ord(haystack[i]) - ord_a) * base) % mod
            else:
                cur_hash = cur_hash - (
                            (ord(haystack[l - 1]) - ord_a) * n_base) % mod  # n_base初始为1则先减去左边界，再加上右边界；否则先加右边界，再减去左边界
                cur_hash = (cur_hash * base) % mod + ((ord(haystack[l + n - 1]) - ord_a) * base) % mod

                # print(l, cur_hash, tar_hash)
            if cur_hash == tar_hash and haystack[l: l + n] == needle:
                return l

        return -1
