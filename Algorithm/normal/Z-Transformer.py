class Solution(object):
    def __init__(self):
        pass

    def z_tranisform(self, str, n):
        if not str or n < 2:
            return str
        res_list = [""] * n
        cur_row = -1
        step_opt = 1

        for chr in str:
            # print(cur_row, step_opt)
            cur_row += step_opt
            res_list[cur_row] += chr
            step_opt = -step_opt if (
                    (cur_row == n - 1 and step_opt == 1) or (cur_row == 0 and step_opt == -1)) else step_opt
        print(res_list)
        return "".join(res_list)


solu = Solution()
str = "aaabcccdd"
n = 3
print(solu.z_tranisform(str, n))
