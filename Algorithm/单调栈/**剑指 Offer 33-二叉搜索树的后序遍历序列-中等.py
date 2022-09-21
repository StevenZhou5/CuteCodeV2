# 剑指 Offer 33. 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
#
#
#
# 参考以下这颗二叉搜索树：
#
# 5
# / \
#     2   6
# / \
#     1   3
# 示例 1：
#
# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：
#
# 输入: [1,3,2,6,5]
# 输出: true
#
#
# 提示：
#
# 数组长度 <= 1000

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 递归 + 分治
        # 时间复杂度：O(n * n)
        # 空间复杂度：O(n), 递归深度最坏情况下一条单链
        # def is_valid(start, end):
        #     if end <= start:
        #         return True
        #     root_val = postorder[end]
        #     left_end = end - 1
        #     while left_end >= 0 and postorder[left_end] > root_val:
        #         left_end -= 1

        #     for i in range(start, left_end):
        #         if postorder[i] > root_val:
        #             return False

        #     return is_valid(start, left_end) and is_valid(left_end + 1, end -1)

        # return is_valid(0, len(postorder) - 1)

        # 单调栈 + 后序遍历的反向遍历
        # 时间复杂度: O(n) 入栈一次，最坏出栈一次
        # 空间复杂度：O(n) 最坏情况全部入栈，只有右子树
        root = float('inf')
        stack = []
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False

            while stack and stack[-1] > postorder[i]:
                root = stack.pop()

            stack.append(postorder[i])
        return True
