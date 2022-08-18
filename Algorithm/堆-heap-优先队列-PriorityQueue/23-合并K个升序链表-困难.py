# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
# 提示：
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> [ListNode]:
        # 优先队列法: 时间复杂度O(kn*lg(k)),空间复杂度O(k)
        if not lists:
            return None
        pq = []
        for idx, cur_node in enumerate(lists):
            if cur_node:
                pq.append([cur_node.val,idx])
        import heapq
        heapq.heapify(pq)

        res_pre = ListNode(0)
        pre = res_pre
        while pq:
            # print(pq)
            cur = lists[pq[0][1]]
            if cur.next:
                lists[pq[0][1]] = cur.next
                heapq.heapreplace(pq, [cur.next.val,pq[0][1]])
            else:
                heapq.heappop(pq)
            pre.next = cur
            pre = cur

            # rebuild(0,len(pq))

        return res_pre.next
