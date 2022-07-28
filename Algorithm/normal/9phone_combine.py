class Solution(object):

    def __init__(self):
        pass

    def get_all_combine(self, str):
        self.num_char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"]
        }
        self.res = []

        def get_combine(cur_target, left_str):
            # 递归终止条件
            if not left_str:
                self.res.append(cur_target)
                return

            for char in self.num_char_map[left_str[0]]:
                get_combine(cur_target + char, left_str[1:])

        get_combine("", str)
        return self.res


solu = Solution()
print("res:", solu.get_all_combine("232"))
