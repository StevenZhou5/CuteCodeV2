# 面试题 16.25. LRU 缓存
# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。
#
# 它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
class ListNode():
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache():
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.key_map = {}
        self.head_node = ListNode()
        self.tail_node = ListNode()
        self.head_node.next = self.tail_node
        self.tail_node.pre = self.head_node

    def put(self, key, val):
        if self.capacity < 1:
            return
        if key in self.key_map:
            node = self.key_map[key]
            node.val = val
            self.change_to_head(node)
            return
        node = ListNode(key, val)
        if self.capacity > len(self.key_map):  # 缓存未满
            self.key_map[key] = node
            self.insert_to_head(node)
            return
        self.remove_tail_node()
        self.insert_to_head(node)
        return

    def get(self, key):
        if self.capacity < 1:
            return -1
        if self.key_map.get(key, None):
            node = self.key_map[key]
            self.change_to_head(node)
            return node.val
        return -1

    def change_to_head(self, node):
        # 把已有结点移动到
        node.pre.next, node.next.pre = node.next, node.pre
        self.insert_to_head(node)
        return

    def insert_to_head(self, node):
        print("is:", self.head_node.next == self.tail_node)
        # print("node:", node.key, node.val)
        # 把一个新结点插入到头部
        self.head_node.next, self.head_node.next.pre, node.pre, node.next = node, node, self.head_node, self.head_node.next
        print("####", self.tail_node.pre, self.head_node.next.val, self.tail_node.pre.key, node.key)
        return

    def remove_tail_node(self):
        # 移除末尾的结点
        node = self.tail_node.pre
        print(node, node.val)
        print(self.key_map)
        self.key_map.pop(node.key)
        self.tail_node.pre, node.pre.next = node.pre, self.tail_node
        return


cache = LRUCache(2)  # /* 缓存容量 */ );

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 返回  1
cache.put(3, 3)  # 该操作会使得密钥 2 作废
print(cache.get(2))  # 返回 -1 (未找到)
cache.put(4, 4)  # 该操作会使得密钥 1 作废
print(cache.get(1))  # 返回 -1 (未找到)
print(cache.get(3))  # 返回  3
print(cache.get(4))  # 返回  4
