class Solution(object):
    def __init__(self):
        pass

    def words_in_matrix(self, words, matrix):
        if not words or not matrix:
            return []
        trie = {}
        is_end_word = "#"
        for word in words:
            cur_node = trie
            for char in word:
                cur_node = cur_node.setdefault(char, {})
            cur_node.setdefault(is_end_word, True)
        print(trie)

        def is_in_trie(word):
            cur_node = trie
            for char in word:
                if cur_node.get(char, None):
                    cur_node = cur_node[char]
                else:
                    return False
            return cur_node.get(is_end_word, False)

        def is_prefix(word):
            cur_node = trie
            for char in word:
                if cur_node.get(char, None):
                    cur_node = cur_node[char]
                else:
                    return None
            return cur_node

        res = set()
        move_i = [-1, 1, 0, 0]
        move_j = [0, 0, -1, 1]
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        def dfs(cur_str, i, j):
            if i < 0 or i >= row_cnt or j < 0 or j >= col_cnt or matrix[i][j] == '.':
                return
            cur_str += matrix[i][j]
            # print("cur_str:%s; i: %d; j:%d" % (cur_str, i, j))
            cur_node = is_prefix(cur_str)
            if cur_node:
                if cur_node.get(is_end_word, False):
                    print("cur_res:", cur_str)
                    res.add(cur_str)
            else:
                return
            tmp_char, matrix[i][j] = matrix[i][j], "."
            for k in range(4):
                dfs(cur_str, i + move_i[k], j + move_j[k])  # 上，下，左，右
            matrix[i][j] = tmp_char
            return

        for i in range(row_cnt):
            for j in range(col_cnt):
                dfs("", i, j)

        return res


solu = Solution()
words = ["word", "hello", "hnodssw", "perssion"]
matrix = [
    ["w", "o", "p"],
    ["s", "r", "e"],
    ["s", "d", "h"],
    ["i", "o", "n"],
]
print("res:", solu.words_in_matrix(words, matrix))
