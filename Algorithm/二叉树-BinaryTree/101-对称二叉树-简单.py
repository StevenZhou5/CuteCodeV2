# 101. 对称二叉树
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
# 提示：
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归 : 核心是左右互相比较
        # 时间复杂度： O(n), 每个节点只访问一次
        # 空间复杂度： O(n), 取决于树的深度，如果只有两条单链
        def recursion(node_left, node_right):
            if not node_left and not node_right:
                return True
            if not node_left or not node_right or node_left.val != node_right.val:
                return False

            return recursion(node_left.left, node_right.right) and recursion(node_left.right, node_right.left)

        return recursion(root.left, root.right)
