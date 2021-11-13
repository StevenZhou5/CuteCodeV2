# 199. 二叉树的右视图
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 示例 2:
#
# 输入: [1,null,3]
# 输出: [1,3]
# 示例 3:
#
# 输入: []
# 输出: []
#
#
# 提示:
#
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100

class Solution():
    def dfs(self, nums):
        if not nums:
            return []
        all_cnt = len(nums)
        visted_level_map = {}
        res = []

        def dfs_with_level(root_idx, cur_level):
            if root_idx > (all_cnt - 1) or not nums[root_idx]:
                return

            if not visted_level_map.get(cur_level, False):  # 没有任何当前层的结点，那么此结点是第一个被看到的当前层的结点
                res.append(nums[root_idx])
                visted_level_map[cur_level] = True
            right_idx = (root_idx << 1) + 2
            dfs_with_level(right_idx, cur_level + 1)
            left_idx = (root_idx << 1) + 1
            dfs_with_level(left_idx, cur_level + 1)

        dfs_with_level(0, 0)
        return res


solu = Solution()
# nums = [1, 2, 3, None, 5, None, 4]
nums = [1, 2, None, None, 3]
print("res:", solu.dfs(nums))
