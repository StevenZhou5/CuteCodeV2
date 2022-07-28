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
    def reverse_with_idx_v2(self, head, left, right):
        if not head or left == right:
            return head

        # 第一步：先找到 left_node 和 left的前一个node
        left_node_pre = head
        left_node = left_node_pre.next
        for _ in range(1, left):
            left_node_pre, left_node = left_node, left_node.next

        # 第二步：反转中间的所有结点，并找到right 和 right 的next结点
        pre = left_node
        cur = pre.next
        for _ in range(right - left):
            cur.next, pre, cur = pre, cur, cur.next
        right_node = pre
        right_node_next = cur

        # 第三步: left_pre.next 等于right; left.next等于 right_next
        left_node_pre.next, left_node.next = right_node, right_node_next

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
left, right = 1, 8
print("left:%d; right:%d;" % (left, right))
solu = Solution()
res_node = solu.reverse_with_idx_v2(head, left, right)
cur = res_node
res = []
while cur:
    res.append(cur.val)
    cur = cur.next
print("res:", res)
