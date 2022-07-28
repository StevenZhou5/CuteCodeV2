# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
# 提示：
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成

class Solution:
    def __init__(self):
        return

    def get_max_prefix_sub_str(self, strs):
        n = len(strs)
        if not n:
            return ""

        trie = {}
        cur_level_trie = trie
        for char in strs[0]:
            cur_level_trie[char] = {}
            cur_level_trie = cur_level_trie[char]

        for i in range(1, n):
            cur_trie = trie
            for char in strs[i]:
                if char not in cur_trie.keys():  # 如果不存在
                    cur_trie.clear()
                    break
                cur_trie = cur_trie[char]

        print("final_trie:", trie)
        res = ""
        cur_final_trie = trie
        while cur_final_trie:
            res = res + list(cur_final_trie.keys())[0]
            cur_final_trie = cur_final_trie[list(cur_final_trie.keys())[0]]
        return res


strs = ["flower", "flow", "floight", "fl"]
solu = Solution()
print("res:", solu.get_max_prefix_sub_str(strs))
