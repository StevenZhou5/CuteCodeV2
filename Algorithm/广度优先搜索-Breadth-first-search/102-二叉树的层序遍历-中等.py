# 102. 二叉树的层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        # 使用dfs也能做: 时间复杂度O(n), 空间复杂度O(n)
        # if not root:
        #     return []
        # self.res = []
        #
        # def dfs(cur_level, node):
        #     if not node:
        #         return
        #     if len(self.res) == cur_level:
        #         self.res.append([])
        #     self.res[cur_level].append(node.val)
        #
        #     dfs(cur_level + 1, node.left)
        #     dfs(cur_level + 1, node.right)
        #
        # dfs(0, root)
        # return self.res

        # bfs + 逐层遍历 ： 时间复杂度O(n), 空间复杂度O(n)
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            cur_level_res = []
            for _ in range(len(queue)):  # 逐层遍历，简化问题
                cur_node = queue.popleft()
                cur_level_res.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(cur_level_res)
        return res
