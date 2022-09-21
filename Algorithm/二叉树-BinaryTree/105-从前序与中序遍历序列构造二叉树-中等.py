# 105. 从前序与中序遍历序列构造二叉树
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 示例 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
# 提示:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        # 递归
        # 时间复杂：O(n),每个节点只访问一次 ;
        # 空间复杂度：O(n), 递归深度
        def recursion(pre_start, pre_end, in_start, in_end):
            # print(pre_start, pre_end, in_start, in_end)
            cur_node = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return cur_node
            mid_idx = in_start
            for i in range(in_start, in_end + 1):
                if inorder[i] == cur_node.val:
                    mid_idx = i
                    break
            left_len = mid_idx - in_start
            right_len = in_end - mid_idx
            cur_node.left = recursion(pre_start + 1, pre_start + left_len, in_start,
                                      in_start + left_len - 1) if left_len > 0 else None
            cur_node.right = recursion(pre_end - right_len + 1, pre_end, in_end - right_len + 1,
                                       in_end) if right_len > 0 else None
            return cur_node

        return recursion(0, len(preorder) - 1, 0, len(inorder) - 1)
