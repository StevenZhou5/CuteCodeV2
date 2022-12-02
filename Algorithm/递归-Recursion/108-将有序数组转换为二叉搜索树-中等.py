# 108. 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
#
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
#
# 示例 2：
#
#
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 按 严格递增 顺序排列

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 递归
        # 时间复杂度：0（n），每个结点遍历一次
        # 空间复杂度：O(log n) 取决于递归的深度
        def recursion(start, end):
            # print(start, end)
            if start > end:
                return None
            if start == end:
                return TreeNode(nums[start])
            mid_idx = start + ((end - start) >> 1)
            return TreeNode(nums[mid_idx], recursion(start, mid_idx - 1), recursion(mid_idx + 1, end))

        return recursion(0, len(nums) - 1)
