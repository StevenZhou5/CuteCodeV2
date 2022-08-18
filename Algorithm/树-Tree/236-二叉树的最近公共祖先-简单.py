# 236. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
# 提示：
#
# 树中节点数目在范围 [2, 105] 内。
# -109 <= Node.val <= 109
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 使用返回参数的递归：时间复杂度O(n), 空间复杂度O(n)-递归调用的空间复杂度取决于树的深度，
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

        # 使用传入参数的递归：时间复杂度O(n), 空间复杂度O(n)

        def findPOrQ(cur_node, p, q):
            # print(cur_node.val, p.val, q.val)
            if not cur_node or cur_node == p or cur_node == q:
                # print(cur_node)
                return cur_node
            left_find = findPOrQ(cur_node.left, p, q)
            right_find = findPOrQ(cur_node.right, p, q)
            # print(cur_node.val, left_find, right_find)
            if left_find and right_find:  # 如果左边找到一个 且 右边找到一个， 当前结点就是最后的最近公共祖先
                return cur_node
            elif not left_find and right_find:  # 如果左边没有找到，右边找到了，返回右边的结点；返回的可能就是最终要找的最近公共结点，或者是向上传递某一分支至少能找到一个
                return right_find
            elif not right_find and left_find:  # 如果右边没有找到，左边找到了，返回左边的结点；
                return left_find

        return findPOrQ(root, p, q)  # 因为p、q是引用对象，内层函数可以直接使用，不传的话速度可能会更快一点，不过为了通用期间还是写上更好
