class Solution(object):
    def __init__(self):
        pass

    def sudoku(self, nums):
        if not nums or len(nums) != 9 or len(nums[0]) != 9:
            return nums
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        board_set = [[set() for _ in range(3)] for _ in range(3)]
        # 记录每行，每列和每个9宫格已经有的数
        for i in range(9):
            for j in range(9):
                if nums[i][j] != '.':
                    cur_val = nums[i][j]
                    row_set[i].add(cur_val)
                    col_set[j].add(cur_val)
                    board_set[i // 3][j // 3].add(cur_val)
            # print(row_set, '\n', col_set, '\n', board_set, '\n', last_i, last_j)
        res = []

        def sodoku_while(nums, starti):
            for i in range(starti, 9):
                for j in range(9):
                    if nums[i][j] != '.':
                        continue
                    for num in range(1, 10):
                        board_i, board_j = i // 3, j // 3
                        if self.is_valid(i, j, board_i, board_j, num, row_set, col_set, board_set):
                            # print("i:%d; j:%d; num:%d" % (i, j, num))
                            nums[i][j] = num
                            row_set[i].add(num), col_set[j].add(num), board_set[board_i][board_j].add(num)

                            if sodoku_while(nums, i):  # 递归, 如果后续都有有效值可以填或者后续都没有需要填充的值
                                return True
                            else:  # 否则回溯，然后试下一个值
                                nums[i][j] = '.'
                                row_set[i].remove(num), col_set[j].remove(num), board_set[board_i][board_j].remove(
                                    num)
                    return False  # 没有一个有效值可以填
            # print("cur_res:", nums)
            res.append(nums.copy())
            return True  # 所有位置都有值

        sodoku_while(nums, 0)
        return res

    def is_valid(self, i, j, board_i, board_j, num, row_set, col_set, board_set):
        # print("i:%d; j:%d; num:%d" % (i, j, num))
        return (num not in row_set[i]) and (num not in col_set[j]) and (num not in board_set[board_i][board_j])


nums = [
    [3, 1, 5, '.', 9, 7, 4, '.', '.'],
    [4, 2, '.', 3, '.', '.', '.', 7, '.'],
    [7, '.', 8, '.', 6, '.', 3, '.', '.'],
    ['.', 6, 4, '.', 2, 9, '.', '.', '.'],
    [8, 3, 9, '.', 7, 4, '.', '.', 2],
    ['.', 7, 2, 1, '.', '.', '.', 9, '.'],
    ['.', '.', '.', 9, 1, '.', 5, 8, '.'],
    ['.', 5, '.', '.', 8, 3, 9, '.', '.'],
    ['.', 8, 1, '.', 4, 5, 2, 3, 6],
]
print("nums:", nums)
solu = Solution()
print("res:", solu.sudoku(nums))
