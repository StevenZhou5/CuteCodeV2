# 255. 验证前序遍历序列二叉搜索树
# 给定一个 无重复元素 的整数数组 preorder ， 如果它是以二叉搜索树的先序遍历排列 ，返回 true 。
#
#
#
# 示例 1：
#
#
#
# 输入: preorder = [5,2,1,3,6]
# 输出: true
# 示例 2：
#
# 输入: preorder = [5,2,6,1,3]
# 输出: false
#
#
# 提示:
#
# 1 <= preorder.length <= 104
# 1 <= preorder[i] <= 104
# preorder 中 无重复元素
#
#
# 进阶：您能否使用恒定的空间复杂度来完成此题？

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # 递归: 会超时
        # 时间复杂度：O(n ^ 2), 最坏情况递归深度为n 每次都要找左右子树的分界点也是n
        # 空间复杂度：O(n), 最坏情况递归深度为n
        # def is_valid(start, end):
        #     # print(start, end)
        #     if start == end:
        #         return True , preorder[start], preorder[start]
        #     # print(start)
        #     root_val = preorder[start]
        #     left_end = start
        #     for i in range(left_end + 1, end + 1):
        #         if preorder[i] > root_val:
        #             break
        #         left_end += 1
        #     is_lfet_valid, left_min, left_max = is_valid(start + 1, left_end) if left_end > start else (True, root_val, root_val - 1)
        #     # print(left_end, start, is_lfet_valid, left_min, left_max)
        #     if not is_lfet_valid or left_max >= root_val:
        #         return False, -1, -1
        #     if left_end + 1 > end: # 右边为空
        #         return True, left_min, root_val
        #     is_right_valid, right_min, right_max = is_valid(left_end + 1, end)
        #     if not is_right_valid or right_min <= root_val:
        #         return False, -1, -1

        #     return True, left_min, right_max

        # res, _, _ = is_valid(0, len(preorder) - 1)
        # return res

        # 单调栈 ： 核心是用一个root_val来记录当前遍历节点的根节点的值，因为右子树后遍历，所以当前root_val存的是最近的左祖先节点的值
        # 时间复杂度：O(n)，所有元素最多入栈和出栈一次，最多2n次操作
        # 空间复杂度：O(n)，要存最长的递减链，最差情况下需要存整个数组的数
        root_val = float('-inf')  # 初始赋值为负无穷，这样可以把所有节点都当做它的右子树
        stack = []  # 单调递减栈，存了root的右儿子的所有左孩子，用于后面回溯，因为每一个左孩子都有当root_val的机会
        for i in range(len(preorder)):
            if preorder[i] < root_val:  # 所有右子树的值都必须大于root_val，否则不合法
                return False
            while stack and preorder[i] > stack[-1]:  # 核心是理解这里，如果已经遍历到 stack[-1] 的右孩子了，那么需要用它更新root_val
                root_val = stack.pop()
            stack.append(preorder[i])
        return True
