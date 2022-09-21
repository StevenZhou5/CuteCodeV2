# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # 链接头尾节点，并找到分割结点
        # 时间复杂度 O(n) n为链表的长度
        # 空间复杂度 O(1)
        # step 1：找到尾结点和 链表长度
        tail = head
        list_len = 1
        while tail.next:
            list_len += 1
            tail = tail.next

        split_poi = list_len - (k % list_len)  # 计算出分割结点的位置
        tail.next = head  # 链接头尾节点， 形成环
        # 初始化分割结点的前继节点
        split_none_pre = tail
        # 找到分割结点
        for _ in range(split_poi):
            split_none_pre = split_none_pre.next
        res = split_none_pre.next
        split_none_pre.next = None
        return res
