# 面试题 01.01. 判定字符是否唯一
# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
#
# 示例 1：
#
# 输入: s = "leetcode"
# 输出: false
# 示例 2：
#
# 输入: s = "abc"
# 输出: true
# 限制：
#
# 0 <= len(s) <= 100
# s[i]仅包含小写字母
# 如果你不使用额外的数据结构，会很加分。

class Solution:
    def isUnique(self, astr: str) -> bool:
        # 位运算 + 状态压缩:
        binary_state = 0
        for c in astr:
            k = ord(c) - ord('a')
            if (binary_state >> k) & 1:
                return False
            binary_state |= (1 << k)
        return True
