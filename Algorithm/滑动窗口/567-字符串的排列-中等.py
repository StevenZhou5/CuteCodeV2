# 567. 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 示例 2：
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
# 提示：
#
# 1 <= s1.length, s2.length <= 104
# s1 和 s2 仅包含小写字母
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口
        # 时间复杂度：O(m + n),都只遍历了一次
        # 空间复杂度：O(m), 只记录了s1的子符频数
        m = len(s1)
        n = len(s2)
        if n < m:
            return False
        distance = m  # 用distance来记录s2子串与s1的距离，
        counter_s1 = collections.Counter(s1)
        counter_s2 = {}
        l, r = 0, 0  # [l, r]用来确定窗口的左右边界
        while r < n:
            if s2[r] in counter_s1:
                counter_s2[s2[r]] = counter_s2.get(s2[r], 0) + 1  # 先进行添加操作可以保证s2[r]的key值存在
                if counter_s2[s2[r]] <= counter_s1[s2[r]]:  # 只有子串字符频数小于目标频数时，添加才会缩小距离，这里使用 <= 是因为先进行的添加操作；
                    distance -= 1

            if r - l == m:  # 此时窗口长度为 m + 1, 所以左边界需要右移一个
                if s2[l] in counter_s1:
                    counter_s2[s2[l]] = counter_s2.get(s2[l], 0) - 1
                    if counter_s2[s2[l]] < counter_s1[s2[l]]:  # 只有子串的字符频数小于等于目标频数时，减少才会增大距离，这里使用 < 是因为先进行了删除操作
                        distance += 1
                l += 1

            if distance == 0:  # 之所以distance == 0 就能保证是返回True，是因为我们固定窗口大小为m；
                return True

            r += 1  # 右边界每次都要右移

        return False
