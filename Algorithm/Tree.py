class TreeNode(object):
    def __init__(self, val=0, left_child=None, right_child=None):
        self.val = val
        self.left = left_child
        self.right = right_child


class TreeUtils():
    def __init__(self):
        super(TreeUtils, self).__init__()

    def common_ancestor(self, head, node1, node2):
        print(head.val, node1.val, node2.val)
        self.result = None

        def is_target_in_child(root):
            if not root:
                return False
            if root == node1 or root == node2:
                return True
            is_left, is_right = is_target_in_child(root.left), is_target_in_child(root.right)
            if is_left and is_right:
                self.result = root
                print("res:", self.result.val)

            return is_left or is_right

        is_target_in_child(head)

        return self.result

    def only_user_pre_traversing(self, head):

        self.pre = -1
        res = []

        def middel(root):
            if not root:
                return

            middel(root.left)
            print("pre_val:%d; cur_val:%d" % (self.pre, root.val))
            self.pre = root.val
            res.append(root.val)
            middel(root.right)

        def first(root):
            if not root:
                return
            res.append(root.val)
            first(root.left)
            first(root.right)

        def last(root):
            if not root:
                return
            last(root.left)
            last(root.right)
            res.append(root.val)

        def dfs(root):
            if not root:
                return
            # 左子树优先等价于先序遍历
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

            # 右子树优先
            # res.append(root.val)
            # dfs(root.right)
            # dfs(root.left)

        def bfs(root):
            if not root:
                return
            from collections import deque

            dq = deque()
            dq.append(root)

            while dq:
                cur_node = dq.popleft()
                res.append(cur_node.val)

                if cur_node.left:
                    dq.append(cur_node.left)
                if cur_node.right:
                    dq.append(cur_node.right)

        def bfs_with_batch(root):
            if not root:
                return
            from collections import deque
            dq = deque()
            dq.append(root)

            while dq:
                cur_vals = []
                for _ in range(len(dq)):  # 每次取出一层
                    node = dq.popleft()
                    cur_vals.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                res.append(cur_vals)

        # middel(head)
        # first(head)
        # last(head)
        # dfs(head)
        # bfs(head)
        bfs_with_batch(head)

        return res

    def max_level(self, head):

        def get_max_level(root):
            if not root:
                return 0

            return 1 + max(get_max_level(root.left), get_max_level(root.right))

        return get_max_level(head)

    def min_level(self, head):
        def get_min_level(root):
            if not root:
                return 0
            min_left = get_min_level(root.left)
            min_right = get_min_level(root.right)
            return (min_left + min_right + 1) if (min_left == 0 or min_right == 0) else (1 + min(min_left, min_right))

        return get_min_level(head)


from collections import deque

head = TreeNode(0)
init_deque = deque()
init_deque.append(head)
node1, node2 = None, None
for i in range(1, 10, 2):
    cur = init_deque.popleft()
    cur.left = TreeNode(i)
    cur.right = TreeNode(i + 1)
    init_deque.append(cur.left)
    init_deque.append(cur.right)
    if cur.right.val == 6:
        node1 = cur.right
    if cur.left.val == 5:
        node2 = cur.left

tu = TreeUtils()
# tu.common_ancestor(head, node1, node2)
print(tu.only_user_pre_traversing(head))

print("最大深度：", tu.max_level(head))
print("最小深度: ", tu.min_level(head))
