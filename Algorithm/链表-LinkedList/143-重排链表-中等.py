# 143. 重排链表
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 示例 2：
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
# 提示：
#
# 链表的长度范围为 [1, 5 * 104]
# 1 <= node.val <= 1000


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 线性表法：时间复杂度O(n),空间复杂度O(n)
        # tmp = []
        # cur = head
        # while cur:
        #     tmp.append(cur)
        #     cur = cur.next
        # i, j = 0 , len(tmp) -1
        # while i < j :
        #     tmp[i].next = tmp[j]
        #     i += 1
        #     if i == j :
        #         break
        #     tmp[j].next = tmp[i]
        #     j -= 1
        # tmp[i].next = None

        # 寻找链表中点 + 链表逆序 + 合并链表 ： 时间复杂度O(n),空间复杂度O(1)
        # step1 : 寻找中间结点
        slow = fast = head
        while fast and fast.next:  # 这样判断的话，奇数个点的时候后半部分会多一个结点
            slow = slow.next
            fast = fast.next.next

        head_middle = slow.next
        slow.next = None

        # step2 ： 后半部分翻转
        pre = None
        cur = head_middle
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp

            # step3 : 合并两个链表
        cur1 = head
        cur2 = pre
        while cur1 and cur2:
            cur1_next = cur1.next
            cur2_next = cur2.next
            cur1.next = cur2
            if cur1_next:  # 因为后cur2在总结点为奇数个的时候会多一个，所以当cur1_next为空时，不能再将cur2.next去指向cur1_next
                cur2.next = cur1_next
            cur1, cur2 = cur1_next, cur2_next
