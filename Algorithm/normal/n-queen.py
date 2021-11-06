class Solution(object):
    def __init__(self):
        pass

    def n_queen(self, n):
        self.res = []
        self.get_(0, set(), set(), set(), [], n)
        print(self.res)
        return [["." * idx + "*" + "." * (n - idx - 1) for idx in items] for items in self.res]

    def get_(self, row, col_set, left_set, right_set, cur_res, n):
        if row == n:
            self.res.append(cur_res.copy())
            return

        for i in range(n):
            cur_left_val, cur_right_val = (i + row), (i - row)
            if i in col_set or cur_left_val in left_set or cur_right_val in right_set:
                continue
            cur_res.append(i), col_set.add(i), left_set.add(cur_left_val), right_set.add(cur_right_val)
            self.get_(row + 1, col_set, left_set, right_set, cur_res, n)
            cur_res.pop(), col_set.remove(i), left_set.remove(cur_left_val), right_set.remove(cur_right_val)


solu = Solution()
print(solu.n_queen(8))
