from random import randint


class QueueToStack():

    def __init__(self):
        print("###########")
        self.a = []
        self.b = []

    def push(self, num):
        if not self.a:  # 如果a 为空， 把b队列的数依次加入a
            self.a.append(num)
            while self.b:
                self.a.append(self.b.pop(0))
        else:
            self.b.append(num)
            while self.a:
                self.b.append(self.a.pop(0))

    def pop(self):
        if self.a:
            return self.a.pop(0)
        if self.b:
            return self.b.pop(0)
        return None


# qts = QueueToStack()
# for i in range(3):
#     qts.push(i)
# for _ in range(2):
#     print("取出数据：%s" % (qts.pop()))
# for i in range(8):
#     qts.push(i)
# for _ in range(10):
#     print("取出数据：%s" % (qts.pop()))


class SlidingWindowMaximum(object):

    def __init__(self):
        super(SlidingWindowMaximum, self).__init__()

    def getMaximun(self, nums, window_size):
        if not nums:
            return None

        can_remove_count = 0
        left_max_dqueue = [nums[0]]
        res = []
        for i in range(1, window_size):
            if nums[i] > left_max_dqueue[0]:
                can_remove_count += len(left_max_dqueue)
                left_max_dqueue.clear()
                left_max_dqueue.append(nums[i])
            else:
                left_max_dqueue.append(nums[i])
        res.append(left_max_dqueue[0])

        for i in range(window_size, len(nums)):
            if can_remove_count > 0:  # 如果还不需要移除最大值
                can_remove_count -= 1  # 移除一个最大值前面的值
                if nums[i] > left_max_dqueue[0]:
                    can_remove_count += len(left_max_dqueue)
                    left_max_dqueue.clear()
                    left_max_dqueue.append(nums[i])
                else:
                    left_max_dqueue.append(nums[i])
            else:
                left_max_dqueue.pop(0)  # 移除最大值
                left_max_dqueue.append(nums[i])  # 添加新值
                # 重新维护left_max_dqueue
                cur_max_idx = 0
                cur_max_num = left_max_dqueue[cur_max_idx]
                for i in range(cur_max_idx, len(left_max_dqueue)):
                    if left_max_dqueue[i] > cur_max_num:
                        cur_max_idx, cur_max_num = i, left_max_dqueue[i]
                left_max_dqueue = left_max_dqueue[cur_max_idx:]
                can_remove_count = cur_max_idx
            res.append(left_max_dqueue[0])
        return res

    def getMaximunV2(self, nums, k):
        if not nums:
            return []
        window_idx = []
        res = []
        for idx, val in enumerate(nums):
            if window_idx and (idx - k) >= window_idx[0]:  # 如果已经需要移除当前最大值了
                window_idx.pop(0)

            while window_idx and val > nums[window_idx[-1]]:  # 如果要加入当前值，那么它前面比他小的值都不需要
                window_idx.pop()

            window_idx.append(idx)  # 把当前值加入到末尾

            if idx >= k - 1:
                res.append(nums[window_idx[0]])

        return res


swm = SlidingWindowMaximum()
nums = [randint(-9, 9) for _ in range(10)]
print(nums)
window_size = 5
print(swm.getMaximun(nums, window_size))
print(swm.getMaximunV2(nums, window_size))
