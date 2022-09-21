class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 时间复杂度O(n), 左右指针最多各遍历一次
        # 空间复杂度O(Σ),其中Σ 表示字符集（即字符串中可以出现的字符），∣Σ∣ 表示字符集的大小。在本题中没有明确说明字符集，因此可以默认为所有 ASCII 码在 [0, 128)[0,128) 内的字符，即 ∣Σ∣=128。我们需要用到哈希集合来存储出现过的字符，而字符最多有∣Σ∣ 个，因此空间复杂度为 O(∣Σ∣)。
        n = len(s)
        counter = {}
        repeat_cnt = 0
        l, r = 0, 0
        res = 0
        while r < n:
            # 移动右边界
            counter[s[r]] = counter.get(s[r], 0) + 1
            if counter[s[r]] > 1:
                repeat_cnt += 1

            # 如果有重复字符移动左边界
            while repeat_cnt > 0:
                counter[s[l]] = counter[s[l]] - 1
                if counter[s[l]] >= 1:
                    repeat_cnt -= 1
                l += 1

            r += 1
            res = max(res, r - l)
        return res
