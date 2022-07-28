# 124. 二叉树中的最大路径和
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
# 提示：
#
# 树中节点数目范围是 [1, 3 * 104]
# -1000 <= Node.val <= 1000

class Solution():
    def get_max_path(self, root):
        # 状态定义：dp[node] 包含当前node和子节点构成的一条最长路径和
        n = len(root)
        res = 0
        for node_idx in range(n - 1, -1, -1):
            left_idx = (node_idx << 1) + 1
            right_idx = left_idx + 1

            left_val = 0 if left_idx >= n else root[left_idx]
            right_val = 0 if right_idx >= n else root[right_idx]
            cur_val = 0 if not root[node_idx] else root[node_idx]

            root[node_idx] = max(cur_val, cur_val + left_val, cur_val + right_val)
            res = max(res, root[node_idx], cur_val + left_val + right_val)
        print(root)
        return res


solu = Solution()
root = [-10, 11, 20, None, None, -15, -7]
print("res:", solu.get_max_path(root))
