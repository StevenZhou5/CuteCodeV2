# 30. 串联所有单词的子串
# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
#
#
#
# 示例 1：
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 示例 3：
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 由小写英文字母组成
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] 由小写英文字母组成
import collections


class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        # 滑动窗口
        # 时间复杂度：时间复杂度：O(ls×n)，其中 ls 是输入 ss 的长度，nn 是 words 中每个单词的长度。需要做 n 次滑动窗口，每次需要遍历一次 s
        # 空间复杂度：O(m×n)，其中 mm 是 words 的单词数，nn 是words 中每个单词的长度。每次滑动窗口时，需要用一个哈希表保存单词频次。

        words_counter = collections.Counter(words)  # 用于快读判断
        word_cnt = len(words)
        word_len = len(words[0])
        n = len(s)
        res = []
        # step1
        for l in range(word_len):
            counter_s = {}
            distance = len(words)
            r = l + word_len

            while r < n + 1:
                # step2：
                cur_word = s[r - word_len: r]
                # print(cur_word, distance)
                if cur_word in words_counter:
                    counter_s[cur_word] = counter_s.get(cur_word, 0) + 1
                    if counter_s[cur_word] <= words_counter[cur_word]:
                        distance -= 1
                # print(cur_word, distance)

                # step3
                if r > l + word_cnt * word_len:  # 如果已经超过所有word字符串长度总和
                    left_word = s[l: l + word_len]
                    if left_word in words_counter:
                        counter_s[left_word] = counter_s[left_word] - 1
                        if counter_s[left_word] < words_counter[left_word]:
                            distance += 1
                    l += word_len
                # print(cur_word, l, r, distance)
                if distance == 0:
                    res.append(l)

                r += word_len

        return res
