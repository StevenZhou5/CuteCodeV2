# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# 3
# / \
#     9  20
# / \
#     15   7
# 返回它的最大深度 3 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs: 时间复杂度 O(n), 空间复杂度O(height) = O(log n) - 取决于递归的深度
        self.max_level = 0

        def dfs(cur_level, node):
            if not node:
                return
            self.max_level = max(self.max_level, cur_level)
            dfs(cur_level + 1, node.left)
            dfs(cur_level + 1, node.right)

        dfs(1, root)
        return self.max_level

        # bfs: 时间复杂度O(n), 空间复杂度O(N)
        # if not root:
        #     return 0
        # from collections import deque
        # max_level = 0
        # queue = deque()
        # queue.append(root)
        #
        # while queue:
        #     max_level += 1
        #     for _ in range(len(queue)):
        #         cur_node = queue.popleft()
        #         if cur_node.left:
        #             queue.append(cur_node.left)
        #         if cur_node.right:
        #             queue.append(cur_node.right)
        #
        # return max_level
