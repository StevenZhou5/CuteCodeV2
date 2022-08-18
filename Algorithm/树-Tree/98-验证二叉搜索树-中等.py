# 98. 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
# 示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
# 提示：
#
# 树中节点数目范围在[1, 104] 内
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归法-使用返回值：时间复杂度O(n),
        # def recursion(node):
        #     if not node.left and not node.right:
        #         return True, node.val, node.val

        #     is_left_valid, left_min, left_max = True, node.val, node.val
        #     if node.left:
        #         is_left_valid, left_min, left_max = recursion(node.left)
        #         if not is_left_valid or left_max >= node.val:
        #             return False, None, None

        #     is_right_valid, right_min, right_max = True, node.val, node.val
        #     if node.right:
        #         is_right_valid, right_min, right_max = recursion(node.right)
        #         if not is_right_valid or right_min <= node.val:
        #             return False, None, None
        #     return True, left_min, right_max
        # is_valid, _, _ = recursion(root)
        # return is_valid

        # 递归法-使用参数法：时间复杂度O(n)
        # def is_valid(node, min_val = float('-inf'), max_val = float('inf')):
        #     if not node:
        #         return True

        #     val = node.val
        #     if min_val >= val or max_val <= val :
        #         return False

        #     if not is_valid(node.left, min_val, val): # 判断左子树时，用当前节点值更新最大值即可
        #         return False

        #     if not is_valid(node.right, val, max_val): # 判断右子树时，用当前节点值更新最小值即可
        #         return False
        #     return True

        # return is_valid(root)

        # 中序遍历法：二叉搜索树的中序遍历是从小到大有序的； 时间复杂度O(n),
        self.pre = float('-inf')

        def inorder_traversal(node):
            if not node:
                return True

            if not inorder_traversal(node.left):
                return False
            # print(self.pre)
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return inorder_traversal(node.right)

        return inorder_traversal(root)
