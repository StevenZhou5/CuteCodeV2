class Backtracking(object):
    def __init__(self):
        super(Backtracking, self).__init__()

    def all_permutation(self, l, change_idx):
        if not l:
            return None
        if change_idx == len(l):
            print(l)
            return

        for i in range(change_idx, len(l)):
            l[change_idx], l[i] = l[i], l[change_idx]  # 和每一个位置交换
            self.all_permutation(l, change_idx + 1)
            l[i], l[change_idx] = l[change_idx], l[i]  # 交换回来

        return


bt = Backtracking()
bt.all_permutation(["a", "b", 'c'], 0)
