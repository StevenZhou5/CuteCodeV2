# 437. 路径总和 III
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
# 示例 2：
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#
#
# 提示:
#
# 二叉树的节点个数的范围是 [0,1000]
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 递归
        # 时间复杂度：O(n * n) 最差情况n个结点每个结点左右n条路径
        # 空间复杂度：O(n)
        # self.res = 0
        # def recursion(node):
        #     if not node:
        #         return []

        #     cur_list = [node.val]
        #     if node.val == targetSum:
        #         self.res += 1
        #     left_list = recursion(node.left)
        #     right_list = recursion(node.right)
        #     for i in range(len(left_list)):
        #         cur_val = node.val + left_list[i]
        #         cur_list.append(cur_val)
        #         if cur_val == targetSum:
        #             self.res += 1

        #     for j in range(len(right_list)):
        #         cur_val = node.val + right_list[j]
        #         cur_list.append(cur_val)
        #         if cur_val == targetSum:
        #             self.res += 1
        #     return cur_list
        # recursion(root)
        # return self.res

        # 前缀和 + 二叉树遍历
        # 时间复杂度：O(n) 每个结点遍历一次
        # 空间复杂度：O(n) 取决于递归深度，最差时O(n)
        prefix_map = collections.defaultdict(int)
        prefix_map[0] = 1  # 前缀和为0的路径初始时有一个，就是根节点的前缀和

        def dfs(node, cur_prefix):
            if not node:
                return 0
            cur_prefix += node.val
            cur_res = prefix_map[cur_prefix - targetSum]  # 只要前缀和等于 cur_prefix - targetSum 的点到当前点的路径都等于targetSum
            prefix_map[cur_prefix] += 1  # 递归到下一层时，当前cur_prefix的前缀和多了1
            left_res = dfs(node.left, cur_prefix)
            right_res = dfs(node.right, cur_prefix)
            prefix_map[cur_prefix] -= 1  # 回到上一层的时候要把后面的前缀和逐一在递归的时候移除
            cur_res = cur_res + left_res + right_res
            return cur_res

        return dfs(root, 0)
