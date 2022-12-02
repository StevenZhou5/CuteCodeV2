# 144. 二叉树的前序遍历
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
# 示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
# 示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 100] 内
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
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        # 递归
        # 时间复杂度： O(n), 每个结点遍历一次
        # 空间复杂度：O(n), 取决于递归的深度
        # self.res = []

        # def recursion(node):
        #     if not node:
        #         return

        #     self.res.append(node.val)
        #     recursion(node.left)
        #     recursion(node.right)
        # recursion(root)
        # return self.res

        # 非递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return res

        # 通用的非递归:
        res = []
        stack = []
        node = root
        while node or stack:
            # 先把左右做孩子按深度依次加入
            while node:
                res.append(node.val)  # 先序遍历放这里
                stack.append(node)
                node = node.left
            node = stack.pop()  # 取出
            node = node.right
        return res
