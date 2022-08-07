class MinHeap(object):
    def __init__(self, nums, k):
        print("###########使用小根堆(优先队列)在n*log(K)的时间复杂度上找到nums中第K大的元素#################")
        self.heap_size = k
        self.heap = nums[:k]
        first_parent = (k - 1 - 1) >> 1
        # print("first_parent:", first_parent)
        for i in range(first_parent, -1, -1):
            self.make_min_heap(i)

    def make_min_heap(self, idx):
        # 保证索引后的堆是小根堆

        left_child_idx = (idx << 1) + 1
        right_child_idx = (idx << 1) + 2
        # print("left_child_idx:", left_child_idx)
        # print("right_child_idx", right_child_idx)

        cur_min_idx = idx
        if left_child_idx < self.heap_size and self.heap[left_child_idx] < self.heap[cur_min_idx]:
            cur_min_idx = left_child_idx
        if right_child_idx < self.heap_size and self.heap[right_child_idx] < self.heap[cur_min_idx]:
            cur_min_idx = right_child_idx

        if idx == cur_min_idx:
            return

        self.heap[idx], self.heap[cur_min_idx] = self.heap[cur_min_idx], self.heap[idx]
        self.make_min_heap(cur_min_idx)


nums = [1, 5, 7, 2, 3, 6, 4, 0, 9]
k = 5
mh = MinHeap(nums, k)
print(mh.heap)

for i in range(5, len(nums)):
    if nums[i] > mh.heap[0]:
        mh.heap[0] = nums[i]
        mh.make_min_heap(0)

print(mh.heap)
