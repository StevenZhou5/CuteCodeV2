class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def __init__(self):
        pass

    def remove_last_k(self, head, k):
        if not head or k <= 0:
            return head
        tar_pre = ListNode
        tar_pre.next = head
        quick_node = head
        for i in range(k):
            quick_node = quick_node.next

        while quick_node:
            quick_node = quick_node.next
            tar_pre = tar_pre.next

        tar_pre.next = tar_pre.next.next if tar_pre.next else None
        return head


from random import randint

head = ListNode(0)
cur = head
k = 0
res_ori = [head.val]
for i in range(1, randint(0, 10)):
    k += 1 if ((randint(1, 2) & 1) == 0) else 0
    cur.next = ListNode(i)
    cur = cur.next
    res_ori.append(cur.val)

print(res_ori, k)
solu = Solution()
res = solu.remove_last_k(head, k)
res_list = []
cur = res
while cur:
    res_list.append(cur.val)
    cur = cur.next
print("res:", res_list)
