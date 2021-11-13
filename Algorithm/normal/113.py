# 113. 路径总和 II
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
# 示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
# 示例 3：
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
# 提示：
#
# 树中节点总数在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

class Solution():

    def get_target_path(self, tree_nums, target_num):
        if not tree_nums or target_num < 1:
            return []
        cnt = len(tree_nums)
        res = []

        def dfs(cur_res, cur_target, root_idx):
            print("cur_res:", cur_res, "root_idx:", root_idx)
            if root_idx >= cnt or not tree_nums[root_idx]:
                return
            cur_val = tree_nums[root_idx]
            cur_res.append(cur_val)
            cur_target += cur_val
            if cur_target == target_num:
                res.append(cur_res)
            dfs(cur_res.copy(), cur_target, (root_idx << 1) + 1)
            dfs(cur_res.copy(), cur_target, (root_idx << 1) + 2)

        dfs([], 0, 0)
        return res


solu = Solution()
tree_nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]  # 模拟树
targetSum = 22
print("res:", solu.get_target_path(tree_nums, targetSum))
