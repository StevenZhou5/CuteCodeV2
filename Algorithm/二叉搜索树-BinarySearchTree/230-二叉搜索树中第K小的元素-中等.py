# 230. 二叉搜索树中第K小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
# 提示：
#
# 树中的节点数为 n 。
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历 + 递归
        # 时间复杂度：O(H + k) ，每个节点访问一次
        # 空间复杂度：O(n) 取决于递归的深度
        # self.idx = 0
        # res = None
        # def recursion(node):
        #     if not node:
        #         return

        #     recursion(node.left)
        #     self.idx += 1
        #     if self.idx == k:
        #         self.res = node.val
        #         return
        #     recursion(node.right)
        # recursion(root)
        # return self.res

        # 中序遍历 + 堆栈
        # 时间复杂度: O (n) 每个结点最多访问一次
        # 空间复杂度：O（n）树的深度最多为n
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left  # 先把做节点都入栈
            root = stack.pop()  # 取出当前节点：左子节点 和 起父节点
            k -= 1
            if k == 0:
                return root.val
            root = root.right  # 左 、 中都访问完了，访问当前的右节点
