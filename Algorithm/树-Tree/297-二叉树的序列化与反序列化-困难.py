# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        # 广度优先逐层遍历 + 哈夫曼编码

        queue = deque()
        queue.append((root, "0"))
        res = ""
        while queue:
            for _ in range(len(queue)):
                node, h_code = queue.popleft()
                res += "#" + h_code + "&" + str(node.val)
                if node.left:
                    queue.append((node.left, h_code + "0"))
                if node.right:
                    queue.append((node.right, h_code + "1"))

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # print(data)
        node_list = data.split("#")
        # print(node_list)
        node_map = {}
        for i in range(1, len(node_list)):
            h_code, node_val = node_list[i].split("&")
            node_map[h_code] = TreeNode(int(node_val))
        # print(node_map)
        queue = deque()
        root = node_map.pop('0')
        queue.append(('0', root))
        while queue:
            for _ in range(len(queue)):
                h_code, node = queue.popleft()
                left_key = h_code + '0'
                if left_key in node_map:
                    node.left = node_map[left_key]
                    queue.append((left_key, node_map.pop(left_key)))
                right_key = h_code + "1"
                if right_key in node_map:
                    node.right = node_map[right_key]
                    queue.append((right_key, node_map.pop(right_key)))
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
