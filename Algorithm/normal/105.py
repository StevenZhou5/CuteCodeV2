# 105. 从前序与中序遍历序列构造二叉树
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 示例 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
# 提示:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均无重复元素
# inorder 均出现在 preorder
# preorder 保证为二叉树的前序遍历序列
# inorder 保证为二叉树的中序遍历序列

class TreeNode():
    def __init__(self, val=0, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class Solution():
    def get_origin_tree(self, preorder, inorder):
        if not preorder:
            return []

        inorder_dict = {num: idx for idx, num in enumerate(inorder)}
        res_dict = {}

        def recursion(preorder_left, preorder_right, inorder_left, inorder_right, level):
            print("preorder_left:", preorder_left, "; preorder_right:", preorder_right, "inorder_left:", inorder_left,
                  ";inorder_right:", inorder_right)
            if preorder_left > preorder_right:  # 只有一个叶子结点
                cur_level_res = res_dict.setdefault(level, [])
                cur_level_res.append(None)  # 需要单独加一个None
                return
            root_val = preorder[preorder_left]
            cur_level_res = res_dict.setdefault(level, [])
            cur_level_res.append(root_val)
            root = TreeNode(root_val)
            if preorder_left == preorder_right:  # 当前结点没有子节点
                next_level_res = res_dict.setdefault(level + 1, [])  # 需要直接在
                next_level_res += [None,None]
                return root

            inorder_root_idx = inorder_dict[root_val]
            len_left = inorder_root_idx - inorder_left
            root.left_child = recursion(preorder_left + 1, preorder_left + len_left, inorder_left,
                                        inorder_root_idx - 1, level + 1)
            root.right_child = recursion(preorder_left + len_left + 1, preorder_right, inorder_root_idx + 1,
                                         inorder_right, level + 1)
            print(root.val, root.left_child, root.right_child)
            return root

        recursion(0, len(preorder) - 1, 0, len(inorder) - 1, 0)
        res = []
        for i in range(len(res_dict) - 1):
            res += res_dict[i]
        return res


# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
# preorder = [-1]
# inorder = [-1]
preorder = [1, 2, 4, 3]
inorder = [4, 2, 1, 3]
solu = Solution()
print("res:", solu.get_origin_tree(preorder, inorder))
