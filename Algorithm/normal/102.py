# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# 3
# / \
#     9  20
# / \
#     15   7
# 返回其层序遍历结果：
#
# [
#     [3],
#     [9,20],
#     [15,7]
# ]

class Solution():

    def bfs_batch(self, nums):
        if not nums:
            return []
        all_cnt = len(nums)
        res = []

        from collections import deque
        queue = deque()
        queue.append(0)
        while queue:
            batch_cnt = len(queue)  # 当前层的结点个数
            cur_res = []
            for _ in range(batch_cnt):
                root_idx = queue.popleft()
                cur_res.append(nums[root_idx])
                left_idx = (root_idx << 1) + 1  # 左边孩子
                if left_idx < all_cnt and nums[left_idx]:
                    queue.append(left_idx)
                right_idx = (root_idx << 1) + 2  # 右边孩子
                if right_idx < all_cnt and nums[right_idx]:
                    queue.append(right_idx)
                # print("left_idx:", left_idx, "right_idx:", right_idx, "; all_cnt:", all_cnt)
            print("cur_res:", cur_res)
            res.append(cur_res)
        return res


solu = Solution()
nums = [3, 9, 20, None, None, 15, 7]
print("res:", solu.bfs_batch(nums))
