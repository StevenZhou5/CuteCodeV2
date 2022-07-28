# 找出游戏中的获胜者

class Solution():

    def get_win_idx(self, n, l):
        if n < 1 or l < 1:
            return -1
        res = [i for i in range(n)]
        cur_remove_idx = (l % len(res)) - 1
        while len(res) > 1:
            if cur_remove_idx == -1:  # 对-1进行修正,-1代表最后一个
                cur_remove_idx = len(res) - 1
            print("len(res):%d ; remove_idx:%d" % (len(res), cur_remove_idx))
            res.pop(cur_remove_idx)
            if cur_remove_idx - 1 + l < len(res):
                cur_remove_idx = cur_remove_idx - 1 + l
            else:
                cur_remove_idx = (l - (len(res) - cur_remove_idx)) % len(res) - 1
        return res[0] + 1


solu = Solution()
# print("res:", solu.get_win_idx(5, 2)) # 3
# print("res:", solu.get_win_idx(6, 5)) # 1
print("res:", solu.get_win_idx(10, 6))  # 3
print("res:", solu.get_win_idx(6, 11))  # 3
