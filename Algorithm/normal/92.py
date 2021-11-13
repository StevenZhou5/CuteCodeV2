# 92. 反转链表 II
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
# 提示：
#
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():

    def reverse_with_idx(self, head, left, right):
        if not head or left == right:
            return

        pre = head
        for _ in range(1, left):
            pre = pre.next
        left_node = pre
        right_node = pre.next
        print(left_node.val, right_node.val)

        cur = pre.next
        for _ in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next
        print("pre:", pre.val, "; cur:", cur.val)
        left_node.next, right_node.next = pre, cur

        return head


solu = Solution()
head = ListNode(0)
cur = head
init = [head.val]
for i in range(1, 10):
    cur.next = ListNode(i)
    cur = cur.next
    init.append(cur.val)
print("init list:", init)

solu = Solution()
res_node = solu.reverse_with_idx(head, 2, 5)
cur = res_node
res = []
while cur:
    res.append(cur.val)
    cur = cur.next
print("res:", res)
