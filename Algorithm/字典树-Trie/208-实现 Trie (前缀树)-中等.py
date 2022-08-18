# 208. 实现 Trie (前缀树)
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
#
# 请你实现 Trie 类：
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
#
#
# 示例：
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
#
# 提示：
#
# 1 <= word.length, prefix.length <= 2000
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

class Trie:

    def __init__(self):
        self.root = {}
        self.end_label = '#'  # 用于标志结束的符号，不能是单词中可能出现的单个字符

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            cur_node = cur_node.setdefault(c, {})
        cur_node[self.end_label] = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        return cur_node.get(self.end_label, False)

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
