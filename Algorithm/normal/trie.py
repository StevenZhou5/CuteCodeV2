class Trie(object):

    def __init__(self):
        self.root = {}
        self.is_end_word = "#"

    def insert(self, word):
        cur_node = self.root
        for char in word:
            cur_node = cur_node.setdefault(char, {})
        cur_node.setdefault(self.is_end_word, True)
        return

    def is_in(self, word):
        cur_node = self.root
        for char in word:
            if cur_node.get(char, None):
                cur_node = cur_node[char]
            else:
                return False
        return cur_node.get(self.is_end_word, False)

    def is_start_with(self, word):
        cur_node = self.root
        for char in word:
            if cur_node.get(char, None):
                cur_node = cur_node[char]
            else:
                return False
        return True


t = Trie()
t.insert("hello")
print(t.root)
print("is_in:", t.is_in("hello"))
print("is_start:", t.is_start_with("hell"))
