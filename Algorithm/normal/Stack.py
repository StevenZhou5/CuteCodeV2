class StackUtils(object):
    def __init__(self):
        super(StackUtils, self).__init__()

    def is_valid_parentheses(self, str):
        print("##########判断括号是否合理##############")

        char_map = {"]": "[", "}": "{", ")": "("}

        stack = []
        for char in str:
            tar_char = char_map.get(char, None)
            if tar_char:
                if stack and tar_char == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

    def sunshine_on_the_tree(self):
        class TreeNode():
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
                self.level = -1

        tree = [TreeNode(i) for i in range(10)]
        tree[0].left, tree[0].right = tree[1], tree[2]
        tree[1].left, tree[1].right = tree[3], tree[4]
        tree[2].left, tree[2].right = tree[5], tree[6]
        tree[5].left, tree[5].right = tree[7], tree[8]
        tree[7].left = tree[9]

        print("##########阳光从右照射进来的每一层的叶子结点###############")

        head = tree[0]
        head.level = 0
        stack = [head]
        fist_map = {}
        result_map = {}
        while stack:
            cur = stack.pop()
            if not fist_map.get(cur.level, None):  # 如果这一层还没有被照射的结点，则添加
                fist_map[cur.level] = cur.val
                if not cur.left and not cur.right:  # 如果没有子节点说明是叶子结点
                    # print("result level%d : %d" % (cur.level, cur.val))
                    result_map[cur.level] = cur.val
            if cur.left:  # 如果有左子结点，把左结点添加到堆栈中
                cur.left.level = cur.level + 1
                stack.append(cur.left)
            if cur.right:  # 如果有右子节点，把右子节点添加到堆栈中
                cur.right.level = cur.level + 1
                stack.append(cur.right)
        print("fist_map:", fist_map)
        print("result_map:", result_map)
        return fist_map, result_map


class StackToQueue():
    def __init__(self):
        print("###########用堆栈实现一个队列###############")
        self.input_stack = []
        self.output_stack = []

    def pop(self):
        print("取数")
        if self.output_stack:
            return self.output_stack.pop()

        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop() if self.output_stack else None

    def push(self, num):
        print("放入数%d" % (num))
        self.input_stack.append(num)


# su = StackUtils()
# str = "[{}]{"
# print("%s 是否合理：%s" % (str, su.is_valid_parentheses(str)))

# su = StackUtils()
# su.sunshine_on_the_tree()

s2q = StackToQueue()
for i in range(10):
    s2q.push(i)
for _ in range(11):
    print(s2q.pop())
