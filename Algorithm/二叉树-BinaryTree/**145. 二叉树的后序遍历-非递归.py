# 145. 二叉树的后序遍历
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
#
#
# 提示：
#
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        # 通用的非递归
        res = []
        stack = []
        node = root
        pre = None  # 后续遍历需要记录pre_node，
        while node or stack:
            # 先把左右做孩子按深度依次加入
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or pre == node.right:  # 如果当前结点没有右节点，或者前一个访问结点就是右节点，此时可以加入结果中
                res.append(node.val)
                pre = node
                node = None
            else:
                stack.append(node)  # 此时还不能访问node，所以要把node加回去
                node = node.right

        return res
