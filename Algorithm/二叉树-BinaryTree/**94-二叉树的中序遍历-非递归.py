# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
# 
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
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
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        # 递归：
        # 时间复杂度：O(n), 每个结点访问一次
        # 空间复杂度: O(log n), 递归的深度
        # res = []
        # def recursion(node):
        #     if not node:
        #         return

        #     recursion(node.left)
        #     res.append(node.val)
        #     recursion(node.right)
        # recursion(root)
        # return res

        # 迭代 + 栈：
        # 时间复杂度: O(n)
        # 空间复杂度: O(n) 当只有左节点一条链时站内会有n个元素
        # res = []
        # stack = []
        # while root or stack:
        #     # 先把所有结点的左节点加进去
        #     while root: # 注意，这里只需要判断root是否为空就行，因为root本身要先入栈，
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     res.append(root.val) # 这里一定是先去一个叶子左节点，然后其right为null，所以下一次回取其父亲结点，然后在把父亲结点的右节点赋值为root
        #     root = root.right
        # return res

        # 通用的非递归
        res = []
        stack = []
        node = root
        while node or stack:
            # 先把左右做孩子按深度依次加入
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()  # 取出
            res.append(node.val)  # 中序遍历放这里
            node = node.right
        return res
