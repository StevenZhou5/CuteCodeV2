class ListNode(object):

    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solutin(object):

    def __init__(self):
        pass

    def merge_two_list(self, head1, head2):
        res = ListNode()
        tail = res
        cur1 = head1
        cur2 = head2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next, cur1 = cur1, cur1.next
            else:
                tail.next, cur2 = cur2, cur2.next
            tail = tail.next
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        return res.next

    def merge_k_list_v1(self, node_list):
        if not node_list:
            return None
        if len(node_list) == 1:
            return node_list[0]
        res = self.merge_two_list(node_list[0], node_list[1])
        for i in range(2, len(node_list)):
            res = self.merge_two_list(res, node_list[i])
        return res

    def merge_k_list_v2(self, node_list):
        if not node_list:
            return None
        if len(node_list) == 1:
            return node_list[0]

        return self.merge_two_list(self.merge_k_list_v2(node_list[0:len(node_list) >> 1]),
                                   self.merge_k_list_v2(node_list[len(node_list) >> 1:]))

    def merge_k_list_v3(self, node_list):
        if not node_list:
            return None
        if len(node_list) == 1:
            return node_list[0]
        min_first_queue = [[i, node_list[i]] for i in range(len(node_list))]
        cnt = len(min_first_queue)

        def reset_min_first_queue(root_idx):
            left_child_idx = (root_idx << 1) + 1
            left_child_val = min_first_queue[left_child_idx][1].val if (
                    left_child_idx < cnt and min_first_queue[left_child_idx][1]) else float("inf")

            right_child_idx = (root_idx << 1) + 2
            right_child_val = min_first_queue[right_child_idx][1].val if (
                    right_child_idx < cnt and min_first_queue[right_child_idx][1]) else float("inf")

            min_idx = root_idx
            min_val = min_first_queue[min_idx][1].val if min_first_queue[min_idx][1] else float('inf')
            if min_val > left_child_val:
                min_idx, min_val = left_child_idx, left_child_val
            if min_val > right_child_val:
                min_idx, min_val = right_child_idx, right_child_val
            if min_idx != root_idx:
                min_first_queue[root_idx], min_first_queue[min_idx] = min_first_queue[min_idx], min_first_queue[
                    root_idx]
                reset_min_first_queue(min_idx)
            return

        last_parent_idx = (cnt - 1) >> 1
        while last_parent_idx >= 0:
            reset_min_first_queue(last_parent_idx)
            last_parent_idx -= 1
        # print(min_first_queue)

        res = ListNode()
        tail = res
        while tail and min_first_queue[0][1]:
            # print("cur_tail:", tail.val)
            tail.next, tail, min_first_queue[0][1] = min_first_queue[0][1], min_first_queue[0][1], min_first_queue[0][
                1].next
            reset_min_first_queue(0)
            # print(min_first_queue)
        return res.next


from random import randint

node_list = []
for i in range(5):
    head1 = ListNode(randint(i, i + 5))
    cur_node = head1
    res = [cur_node.val]
    for _ in range(randint(0, 5)):
        cur_node.next = ListNode(cur_node.val + randint(0, 5))
        cur_node = cur_node.next
        res.append(cur_node.val)
    print(res)
    node_list.append(head1)

solu = Solutin()
# res = solu.merge_k_list_v2(node_list)
res = solu.merge_k_list_v3(node_list)
cur_node = res
res_list = []
while cur_node:
    res_list.append(cur_node.val)
    cur_node = cur_node.next
print(res_list)
