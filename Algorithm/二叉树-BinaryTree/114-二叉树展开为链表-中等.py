# 114. 二叉树展开为链表
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
#
# 示例 1：
#
#
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [0]
# 输出：[0]
#
#
# 提示：
#
# 树中结点数在范围 [0, 2000] 内
# -100 <= Node.val <= 100
#
#
# 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 递归
        # 时间复杂度O(n), 每个结点访问一次
        # 空间复杂度O(n), 取决于递归的深度，最坏的单链表情况下，递归深度等于n
        def recursion(node):  # 返回单链条的头节点 ， 尾结点
            if not node:
                return None, None
            if not node.left and not node.right:  # 叶子结点的头尾节点一直
                return node, node

            left_head, left_end = recursion(node.left)
            right_head, right_end = recursion(node.right)
            if left_head:  # 只有左节点不为None，才需要链接左右
                node.right = left_head  # 把左节点的头节点链接到当前节点的右节点上
                node.left = None  # 同事把当前结点的左节点删除
                left_end.right = right_head  # 左节点的尾结点链接到右边的头节点上
            return node, right_end if right_end else left_end  # 合并完的头节点就是当前结点，合并完的尾结点要看右节点是否为空：为空的话需要返回左节点的尾结点

        recursion(root)
