# 24. 两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归法 : 时间复杂度O(n); 空间复杂度O(n)
        # if not head or not head.next:
        #     return head
        # res = head.next
        # head.next = self.swapPairs(res.next)
        # res.next = head

        # return res

        # 迭代法 : 时间复杂度O(n); 空间复杂度O(1)
        res = ListNode(0)
        res.next = head
        pre = res
        while pre.next and pre.next.next:
            a, b, c = pre.next, pre.next.next, pre.next.next.next
            pre.next, b.next, a.next = b, a, c
            pre = a

        return res.next
