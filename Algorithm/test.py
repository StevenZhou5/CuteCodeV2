class TreeNode():
    def __init__(self, val, left_child, right_child):
        self.val = val  # 代表以当前值结尾的子序列的长度
        self.left_child = left_child
        self.right_child = right_child


class Solution():

    def add_min_stack(self, root, new_val):
        if not root:
            return TreeNode(new_val, None, None)

        if root.val > new_val:
            root.val, new_val = new_val, root.val

        if not root.left_child:
            root.left_child = self.add_min_stack(root.left_child, new_val)
            return root

        if not root.right_child:
            root.right_child = self.add_min_stack(root.right_child, new_val)
            return root

        if root.left_child.val > root.right_child.val:
            root.left_child = self.add_min_stack(root.left_child, new_val)
        else:
            root.right_child = self.add_min_stack(root.right_child, new_val)
        return root

    def reset_min_stack(self, root):
        if not root or (not root.left_child and not root.right_child):
            return

        target_node = root.left_child if not root.right_child or root.right_child.val > root.left_child.val else root.right_child
        if root.val > target_node.val:
            root.val, target_node.val = target_node.val, root.val
            self.reset_min_stack(target_node)

    def remove_min_stack_head(self, root):
        if not root.left_child and not root.right_child:
            return None

        if not root.left_child:
            target_node = root.right_child
        elif not root.right_child:
            target_node = root.left_child
        else:
            target_node = root.left_child if root.right_child.val > root.left_child.val else root.right_child
        root.val = target_node.val
        if target_node == root.left_child:
            root.left_child = self.remove_min_stack_head(root.left_child)
        else:
            root.right_child = self.remove_min_stack_head(root.right_child)
        return root

    def isPossible(self, num_list):
        stack_dick = {}
        for num in num_list:
            node_pre = stack_dick.get(num - 1, None)
            if not node_pre:  # 如果没有以 num-1结尾的子序列，那么需要建立一个长度为1以num结尾的子序列
                node_num = stack_dick.get(num, None)
                stack_dick[num] = self.add_min_stack(node_num, 1)
            else:
                # 需要将向num中添加一个长度为node_pre.val + 1的数据
                node_num = stack_dick.get(num, None)
                stack_dick[num] = self.add_min_stack(node_num, node_pre.val + 1)

                # 同时需要把node_pre中最顶部的结点删除
                node_pre = self.remove_min_stack_head(node_pre)
                stack_dick[num - 1] = node_pre

        print(stack_dick)
        for k, v in stack_dick.items():
            print(k, v.val if v else None)
            if v and v.val < 3:
                return False
        return True

    def get_min_step(self, s1, s2):
        if not s1 and not s2:
            return 0
        m, n = len(s1), len(s2)
        if not m or not n:
            return max(m, n)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i - 1][j] + 1
                left = dp[i][j - 1] + 1
                up_left = dp[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                # print((i, j), "up:", up, "; left:", left, "; up_left:", up_left)
                dp[i][j] = min(up, left, up_left)
        print(dp)
        return dp[m][n]


s = Solution()
# s.can_split([1, 2, 3, 4, 5, 6])
# s.can_split([1,2,3,3,4,4,5,5])
# s.can_split([1,2,3,3,4,5])
# s.can_split([1,2,3,3,4,4,5])
# s.can_split([1,2,2,3])
# [[0, inf, 2],
#  [0, inf, 2],
#  [0, inf, 2],
#  [0, inf, 2],
#  [0, inf, 2]]
print("res:", s.get_min_step("acbs", "abds"))
