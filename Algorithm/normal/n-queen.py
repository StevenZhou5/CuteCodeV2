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

    def n_queen_binary(self, n):
        if not n:
            return []

        res = []

        def recursion(row, col_state, left_state, right_state, cur_state):
            # print(row, col_state, left_state, right_state, cur_state)
            if row >= n:
                res.append(["*" * cur_state[i] + "Q" + "*" * (n - cur_state[i] - 1) for i in range(n)])
                return
            not_valid_pos = col_state | left_state | right_state
            # print("valid_pos:", valid_pos)
            col = 0
            while col < n:
                if not not_valid_pos & 1:  # 当前列可用
                    # print("当前行列：", row, col)
                    cur_col_state = 1 << col
                    cur_state.append(col)
                    recursion(row + 1, col_state | cur_col_state, (left_state | cur_col_state) << 1,
                              (right_state | cur_col_state) >> 1, cur_state)
                    cur_state.pop()
                col += 1
                not_valid_pos >>= 1

        recursion(0, 0, 0, 0, [])
        return res


solu = Solution()
# print("res1:", solu.n_queen(8))
print("res2", solu.n_queen_binary(4))
