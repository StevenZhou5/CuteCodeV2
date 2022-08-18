# 111. 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 示例 2：
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
# 提示：
#
# 树中节点数的范围在 [0, 105] 内
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # bfs : 时间复杂O(n), 空间复杂度O(n)
        # if not root:
        #     return 0
        # cur_level = 0
        # from collections import deque
        # queue = deque()
        # queue.append(root)

        # while queue:
        #     cur_level += 1
        #     for _ in range(len(queue)):
        #         cur_node = queue.popleft()
        #         if not cur_node.left and not cur_node.right:
        #             return cur_level
        #         if cur_node.left:
        #             queue.append(cur_node.left)
        #         if cur_node.right:
        #             queue.append(cur_node.right)

        # dfs : 时间复杂度O(n), 空间复杂度O(height) = O(log n)
        # if not root:
        #     return 0
        # self.min_level = float('inf')
        # def dfs(cur_level, node):
        #     if not node:
        #         return
        #     if not node.left and not node.right and cur_level < self.min_level:
        #         self.min_level = cur_level
        #     dfs(cur_level + 1, node.left)
        #     dfs(cur_level + 1, node.right)
        # dfs(1, root)
        # return self.min_level

        # 分治 + 递归：时间复杂度O(n), 空间复杂度O(log n)
        if not root:
            return 0
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        return left_min + right_min + 1 if not left_min or not right_min else 1 + min(left_min, right_min)
