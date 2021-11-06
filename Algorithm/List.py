import random


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListUtils(object):
    def __init__(self, init_with_cycle=False, cycle_node_idx=1):
        self.head = ListNode(0)
        cur = self.head
        for i in range(1, 100):
            # cur.next = ListNode(i + cur.val)
            cur.next = ListNode(i)
            cur = cur.next
        if init_with_cycle:
            cycle_node = self.head
            for _ in range(cycle_node_idx):
                cycle_node = cycle_node.next
            cur.next = cycle_node
        else:
            cur = self.head
            while cur:
                print(cur.val)
                cur = cur.next
        super(ListUtils, self).__init__()

    def rever_list(self):
        print("+++++++revert++++++++++")
        cur, pre = self.head, None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur

        cur = pre
        while cur:
            print(cur.val)
            cur = cur.next

    def two_num_change(self):
        print("+++++++two_num_change++++++++++")
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
        new_head = self.head.next
        pre = ListNode()  # 如果赋值为self 或者一个空的ListNode()，那么不需要做判空处理
        cur = self.head
        while cur and cur.next:  # 每次交换两个，移动两个
            print("cur_val:%d; next_val:%d" % (cur.val, cur.next.val))
            next = cur.next
            next_cur = next.next
            # if pre:
            pre.next = next
            cur.next, next.next, pre, cur = next_cur, cur, cur, next_cur  # 交换

            # pre = cur
            # cur = next_cur

        cur = new_head
        while cur:
            print(cur.val)
            cur = cur.next

    def has_cycle(self):
        slow = self.head
        quick = self.head
        print("+++++++判断是否有环++++++++++")
        while slow and quick:
            slow = slow.next
            quick = quick.next
            quick = quick.next if quick else None
            if slow == quick:
                print("有环")
                return True
        print("无环")
        return False

    def find_cycle_node(self):
        print("+++++++寻找到环结点++++++++++")
        slow = self.head
        quick = self.head
        while True:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                print("第一次相遇，相遇结点为:%d" % (slow.val))
                break
        slow = self.head
        while slow != quick:
            slow = slow.next
            quick = quick.next

        print("第二次相遇在环结点，环结点为:%d" % (slow.val))
        return slow

    def find_first_cross_node(self):
        cross_idx = 8
        head1 = ListNode(0)
        cur1 = head1
        head2 = ListNode(0)
        cur2 = head2
        for i in range(1, 10):
            if i < cross_idx:
                if random.randint(0, 9) in [1, 2, 3]:
                    cur1.next = ListNode(random.randint(0, 9))
                    cur1 = cur1.next
                else:
                    cur2.next = ListNode(random.randint(0, 9))
                    cur2 = cur2.next
            else:
                cur1.next = cur2.next = ListNode(i)
                cur1 = cur1.next
                cur2 = cur2.next

        print("+++++++寻找第一个公共结点++++++++++")
        # step1 : 得到两个链表的长度
        cur1 = head1
        len1 = 1
        while cur1:
            print("链表1：%d" % (cur1.val))
            cur1 = cur1.next
            len1 += 1
        print("+++++++len1:%d+++++++++" % (len1))

        cur2 = head2
        len2 = 1
        while cur2:
            print("链表2：%d" % (cur2.val))
            cur2 = cur2.next
            len2 += 1
        print("++++++++len2:%d++++++++" % (len2))

        short, long, d_len = (head1, head2, len2 - len1) if len1 < len2 else (head2, head1, len1 - len2)
        for _ in range(d_len):
            long = long.next

        while short != long:
            short = short.next
            long = long.next

        print("第一个交叉结点为:%d" % (short.val))
        return short


# list_utils = ListUtils()
# list_utils.rever_list()

# list_utils = ListUtils()
# list_utils.two_num_change()

# list_utils = ListUtils(init_with_cycle=True)
# list_utils.has_cycle()

# list_utils = ListUtils(init_with_cycle=True, cycle_node_idx=10)
# list_utils.find_cycle_node()

list_utils = ListUtils()
list_utils.find_first_cross_node()
