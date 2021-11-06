class Solution(object):

    def __init__(self):
        pass

    def get_median(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            cnt2 = len(list2)
            return (list2[(cnt2 - 1) >> 1] + list2[cnt2 >> 1]) / 2  # 如果cnt是奇数，两个idx相等，如果是偶数，一个是左一个是右边
        if not list2:
            cnt1 = len(list1)
            return (list1[(cnt1 - 1) >> 1] + list1[cnt1 >> 1]) / 2
        cnt1, cnt2, idx1, idx2 = len(list1), len(list2), 0, 0
        mid_left_idx, mid_right_idx = (cnt1 + cnt2 - 1) >> 1, (cnt1 + cnt2) >> 1
        print(mid_left_idx, mid_right_idx)
        merge_cnt = -1
        res = 0
        while idx1 < cnt1 or idx2 < cnt2:
            val1 = list1[idx1] if idx1 < cnt1 else float('inf')
            val2 = list2[idx2] if idx2 < cnt2 else float('inf')
            cur_val = 0
            if val1 <= val2:
                cur_val = list1[idx1]
                idx1 += 1
            else:
                cur_val = list2[idx2]
                idx2 += 1

            merge_cnt += 1

            if merge_cnt == mid_left_idx:
                print("left_val:", cur_val)
                res += cur_val
            if merge_cnt == mid_right_idx:
                print("right_val:", cur_val)
                res += cur_val
                break

        return res / 2


from random import randint

list1 = [randint(-10, 10) for _ in range(randint(0, 10))]
list1 = sorted(list1)
# list1 = []
list2 = [randint(-10, 10) for _ in range(randint(0, 10))]
list2 = sorted(list2)
print("list1:", list1)
print("list2:", list2)
solu = Solution()
print("res :", solu.get_median(list1, list2))
