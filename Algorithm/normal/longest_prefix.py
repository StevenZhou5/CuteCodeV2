class Solution(object):

    def __init__(self):
        pass

    def get_longest_prefix(self, str_list):
        if not str_list:
            return ""
        res_idx = 0
        for i in range(len(str_list[0])):
            cur_char = str_list[0][i]
            for str in str_list[1:]:
                if len(str) <= i or str[i] != cur_char:
                    break
            else:  # 直接让break跳出上一层的循环,如果内循环没有break,则执行else地下的逻辑
                res_idx += 1

        return str_list[0][:res_idx]


solu = Solution()
str_list = ["assd", "as", "asff"]
print("res:", solu.get_longest_prefix(str_list))
