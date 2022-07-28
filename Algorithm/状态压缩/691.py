# 691. 贴纸拼词
# 我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。
#
# 你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 target。
#
# 如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。
#
# 拼出目标 target 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。
#
#
#
# 示例 1：
#
# 输入：
#
# ["with", "example", "science"], "thehat"
# 输出：
#
# 3
# 解释：
#
# 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
# 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
# 此外，这是形成目标字符串所需的最小贴纸数量。
# 示例 2：
#
# 输入：
#
# ["notice", "possible"], "basicbasic"
# 输出：
#
# -1
# 解释：
#
# 我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
#
#
# 提示：
#
# stickers 长度范围是 [1, 50]。
# stickers 由小写英文单词组成（不带撇号）。
# target 的长度在 [1, 15] 范围内，由小写字母组成。
# 在所有的测试案例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选取的，目标是两个随机单词的串联。
# 时间限制可能比平时更具挑战性。预计 50 个贴纸的测试案例平均可在35ms内解决。

class Solution():
    def need_min_cnt_dp_sc(self, stickers, target):
        # target中的每一位字符是否已经被匹配用二进制为表示，1代表还没有被匹配，0代表已经匹配
        # 状态定义 dp[0000 0000 0000 0000] 代表所有字符都被匹配了；target长度最大为16，所以只需要最多16位二进制数就能表示
        dp = {}  # 当前状态下所需要的最少个数
        target_len = len(target)
        final_state = (1 << target_len) - 1
        print("final_state:", final_state)

        from collections import Counter
        sticker_char_cnt_map_list = []
        for word in stickers:
            sticker_char_cnt_map_list.append(Counter(word))

        def recursion(cur_state):
            # 递归终止条件
            if cur_state == 0:
                dp[cur_state] = 0
                return 0
            if cur_state in dp:
                return dp[cur_state]

            min_use_cnt = float('inf')
            for char_cnt_map in sticker_char_cnt_map_list:  # 遍历每个单词生成的字符cnt统计值,每个单词可以用无限次，因此也不需要判断这个单词是否被用了
                tmp_cnt_map = char_cnt_map.copy()
                update_state = 0  # 选择此单词后，可以进行的状态更新
                for i in range(target_len):  # 遍历单词中的每一个位置，进行字符匹配
                    need_i = (cur_state >> i) & 1 == 1  # 如果对应二进制位 ==1 说明需要
                    if not need_i or tmp_cnt_map.get(target[i], 0) <= 0:  # 如果当前位置字符已经匹配 或者 当前剪切出的字符中没有目标字符
                        continue
                    # 匹配到了
                    update_state += (1 << i)  # 第i个位置被匹配了
                    tmp_cnt_map[target[i]] = tmp_cnt_map[target[i]] - 1  # 对应用掉了一个字符
                # 选择此单词不能带来任何状态更新，那么不选词单词
                if update_state == 0:
                    continue
                # 选择此单词，并进行最小使用单词的更新
                min_use_cnt = min(min_use_cnt, recursion(cur_state - update_state) + 1)

            dp[cur_state] = min_use_cnt
            return min_use_cnt

        res = recursion(final_state)
        print("dp:", dp)
        return -1 if res == float('inf') else res


solu = Solution()
# stickers, target = ["with", "example", "science"], "thehat"
# stickers, target = ["notice", "possible"], "basicbasic"
stickers, target = ["notice", "possible"], "noticez"
print("res:", solu.need_min_cnt_dp_sc(stickers, target))
