class QuickSort(object):
    def sort(self, nums):
        if not nums:
            return

        # step1
        def go_step(nums, left, right):
            if left >= right:
                return

            start = left
            end = right
            target = nums[left]
            while start < end:
                if nums[end] >= target and start < end:
                    end -= 1
                if nums[start] <= target and start < end:
                    start += 1
                if start < end:
                    nums[start], nums[end] = nums[end], nums[start]

            nums[left], nums[end] = nums[end], nums[left]
            go_step(nums, left, end - 1)
            go_step(nums, end + 1, right)

        go_step(nums, 0, len(nums) - 1)


class MergeSort(object):
    def sort(self, nums):
        if len(nums) <= 1:
            return

        def merge_two_nums(nums_left, nums_right):
            if not nums_left or not nums_right:  # 如果有一组为空的话
                return nums_left + nums_right
            middle_left_idx = len(nums_left) >> 1
            nums_left = merge_two_nums(nums_left[0:middle_left_idx], nums_left[middle_left_idx:])

            middle_right_idx = len(nums_right) >> 1
            nums_right = merge_two_nums(nums_right[0:middle_right_idx], nums_right[middle_right_idx:])

            res = []
            cur_left_idx = 0
            cur_right_idx = 0
            while nums_left and nums_right:
                if nums_left[cur_left_idx] <= nums_right[cur_right_idx]:
                    res.append(nums_left.pop(0))
                else:
                    res.append(nums_right.pop(0))

            return res + nums_left + nums_right

        middle_idx = len(nums) >> 1
        return merge_two_nums(nums[0:middle_idx], nums[middle_idx:])


# num_sort = QuickSort()
# num_sort = MergeSort()
# nums = [5, 4, 3, 2, 1, 1, 1, 5, 5, 3]
# print("start:", nums)
# nums = num_sort.sort(nums)
# print("end:", nums)

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rever_list():
    head = ListNode(1)
    cur = head
    for i in range(1, 5):
        cur.next = ListNode(i + cur.val)
        cur = cur.next
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

    print("+++++++revert++++++++++")
    cur, pre = head, None
    while cur:
        cur.next, cur, pre = pre, cur.next, cur

    cur = pre
    while cur:
        print(cur.val)
        cur = cur.next


# rever_list()

def two_num_change():
    head = ListNode(1)
    cur = head
    for i in range(1, 7):
        cur.next = ListNode(i + cur.val)
        cur = cur.next
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

    print("+++++++revert++++++++++")
    # 实现1
    # new_head = head.next
    # pre = None
    # cur = head
    # while cur:
    #     print("cur_val:", cur.val)
    #     if cur.next:
    #         # 先交换两个node
    #         if pre:
    #             cur.next.next, cur.next, pre.next, pre, cur = cur, cur.next.next, cur.next, cur, cur.next.next
    #         else:
    #             cur.next.next, cur.next, pre, cur = cur, cur.next.next, cur, cur.next.next
    #     else:
    #         cur = cur.next

    # 实现2
    new_head = head.next
    pre = None
    cur = head
    while cur and cur.next:  # 每次交换两个，移动两个
        print("cur_val:%d; next_val:%d" % (cur.val, cur.next.val))
        next = cur.next
        next_cur = next.next
        if pre:
            pre.next = next
        cur.next, next.next, pre, cur = next_cur, cur, cur, next_cur  # 交换

        # pre = cur
        # cur = next_cur

    cur = new_head
    while cur:
        print(cur.val)
        cur = cur.next
