# 543. 二叉树的直径
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
# 1
# / \
#     2   3
# / \
#     4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 递归
        # 时间复杂O(n): 每个结点最多访问一次
        # 空间复杂度O(n), 取决于递归深度，最坏单链情况下O(n)
        self.res = 0

        def get_max(node):
            if not node:
                return 0
            left_max = get_max(node.left)
            right_max = get_max(node.right)
            self.res = max(self.res, left_max + right_max)
            return max(left_max, right_max) + 1

        get_max(root)
        return self.res
