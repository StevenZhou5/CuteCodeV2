# 424. 替换后的最长重复字符
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
#
# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。
#
#
#
# 示例 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 示例 2：
#
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由大写英文字母组成
# 0 <= k <= s.length
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 滑动窗口
        # 时间复杂度O(n), 最多左右指针各移动一次
        # O(∣Σ∣)，其中∣Σ∣ 是字符集的大小。我们需要存储每个大写英文字母的出现次数。
        n = len(s)
        # step1:
        counter = {}
        counter_max = s[0]  # 窗口内数量最多的字符为
        # opt_cnt = 0 # 操作次数
        l, r = 0, 0
        res = 0

        while r < n:
            # step2: 右移
            counter[s[r]] = counter.get(s[r], 0) + 1
            if counter[s[r]] > counter[counter_max]:
                counter_max = s[r]

            # step3:左移,其实这里只要最多字符需要k + 1次操作时就会移动左边界，左边界只要移动到需要k次时就会停止，此时在当前窗口中此字符任然是满足条件的最多字符：因为counter[counter_max] - 1就会终止，那么-1之后的数目一定是大于等于第二多的字符的；
            if (r - l + 1) - counter[counter_max] > k:  # 如果数量最多的字符需要操作的次数都超过k了
                counter[s[l]] = counter[s[l]] - 1  #
                l += 1

            r += 1
            # step4
            res = max(r - l, res)
        return res
