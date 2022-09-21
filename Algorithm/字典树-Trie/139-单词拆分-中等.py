# 139. 单词拆分
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
# 提示：
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # trie + 动态规划：
        # 时间复杂度：O(max(n, m) * max(len(word))) :n 为s的长度，m为wordDict的长度
        # 空间复杂度：O(n + m) 存储字典树最多为O(m)，最初状态dp为O(n)
        END_LABEL = "#"
        trie_root = {}
        for word in wordDict:
            cur_trie_node = trie_root
            for c in word:
                cur_trie_node = cur_trie_node.setdefault(c, {})
            cur_trie_node[END_LABEL] = True
        # print(trie_root)
        n = len(s)
        # 状态定义
        dp = [False] * (n + 1)  # dp[i] 代表以第i个字符为起始位置到末尾所有字符是否可以使用wordDict来构建
        dp[-1] = True  # 在末尾加上一个哨兵，代表空字符串
        for i in range(n - 1, -1, -1):  # 因为字典树是正序构建的，所以动态规划的遍历从末尾来遍历
            cur_node = trie_root
            for j in range(i, n):
                # print(s[i], s[j])
                if not cur_node.get(s[j], None):  # 如果不含当前字符
                    break
                cur_node = cur_node[s[j]]
                # 状态转移
                if cur_node.get(END_LABEL, False) and dp[j + 1]:
                    dp[i] = True
                    break

        # print(dp)
        return dp[0]
