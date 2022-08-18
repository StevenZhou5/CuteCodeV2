# 235. 二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:
#
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#
#
# 说明:
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 通用方法(即使不是二叉搜索树也适用)：时间复杂度O(n), 空间复杂度O(n)-递归取决于递归的深度
        # self.is_first = True
        # self.res = None

        # def dfs(node):
        #     if not node:
        #         return False, False

        #     left_has_p, left_has_q = dfs(node.left)
        #     right_has_p, right_has_q = dfs(node.right)
        #     has_p = node == p or left_has_p or right_has_p
        #     has_q = node == q or left_has_q or right_has_q
        #     # print(node.val, has_p, has_q)
        #     if self.is_first and has_p and has_q:
        #         # print(node.val)
        #         self.res = node
        #         self.is_first = False
        #     return has_p, has_q
        # dfs(root)
        # return self.res

        # 利用二叉搜索树特性（最近公共祖先的值一定介于两者值之间）： 时间复杂度O(n), 空间复杂度O(1)-非递归空间复杂度更优
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        cur_node = root
        while cur_node:
            if min_val <= cur_node.val <= max_val:
                return cur_node
            elif cur_node.val < min_val:
                cur_node = cur_node.right
            else:  # cur_node.val > max_val
                cur_node = cur_node.left

        return None
