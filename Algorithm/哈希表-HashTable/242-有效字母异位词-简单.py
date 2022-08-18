# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#
#
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 使用固定数组下标作为hash: 时间复杂度 O(n), 空间复杂度O(26)
        # counter_list = [0] * 26

        # for c in s:
        #     counter_list[ord(c) - ord('a')] += 1

        # # print(counter_list)
        # for c in t:
        #     idx = ord(c) - ord('a')
        #     if not counter_list[idx]:
        #         return False
        #     counter_list[idx] -= 1

        # return sum(counter_list) == 0

        # 使用字典实现:时间复杂度O(n), 空间复杂度O(s) s为不同字母的个数
        # counter_map = {}
        # for c in s:
        #     count = counter_map.setdefault(c, 0)
        #     counter_map[c] = count + 1
        #
        # for c in t:
        #     count = counter_map.setdefault(c, 0)
        #     # if not count:
        #     #     return False
        #     counter_map[c] = count - 1
        #
        # for k, v in counter_map.items():
        #     if v != 0:
        #         return False
        #
        # return True

        #  使用两个dict
        counter_s, counter_t = {}, {}
        for c in s:
            counter_s[c] = counter_s.get(c, 0) + 1
        for c in t:
            counter_t[c] = counter_t.get(c, 0) + 1
        return counter_s == counter_t
