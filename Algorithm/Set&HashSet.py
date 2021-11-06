from random import randint


class SetUtils(object):
    def __init__(self):

        super(SetUtils, self).__init__()

    def two_sums(self, nums, target):
        if not nums or len(nums) < 2:
            return []

        se = set()
        res = set()
        for val in nums:
            another = target - val
            if another in se:
                res.add((another, val))
            se.add(val)

        return res

    def two_sums_idx(self, nums, target):
        if not nums or len(nums) < 2:
            return {}

        mp = {}
        res = set()
        for idx, val in enumerate(nums):
            another = target - val
            if another in mp:
                res.add((mp[another], idx))
            mp[val] = idx

        return res

    def three_sums(self, nums, target):
        if not nums or len(nums) < 3:
            return {}

        nums = sorted(nums)  # 排序可以有助于后续相同元素的判断
        print(nums)

        res = set()

        last_first = None
        for idx1 in range(len(nums) - 2):
            first = nums[idx1]
            if first == last_first:  # 因为排过序，不需要再判断
                continue
            last_first = first

            last_second = None
            thread_target_set = set()
            for idx2 in range(idx1 + 1, len(nums)):
                second = nums[idx2]
                if second == last_second:
                    continue
                last_second = second

                thread_target = target - (first + second)  # 需要找的第三个值
                if second not in thread_target_set:  # 如果当前值并不是前面组合中的第三个target
                    thread_target_set.add(thread_target)  # 把要找的新的target 加入进去
                else:  # 此时的second 是前面组合中的一个目标值

                    res.add((first, thread_target, second))  # 注意 此时thread_target是第二个出现的值, 此时的second才是最后要找的值

        return res

    def three_sums_v2(self, nums, target):
        if not nums or len(nums) < 3:
            return []
        nums = sorted(nums)
        count = len(nums)
        res = set()
        for first_idx in range(count):
            second_idx = first_idx + 1
            third_idx = count - 1

            while second_idx < third_idx:
                cur_sum = nums[first_idx] + nums[second_idx] + nums[third_idx]
                if cur_sum == target:
                    res.add((nums[first_idx], nums[second_idx], nums[third_idx]))  # 找到一组接
                    second_idx += 1
                    third_idx -= 1
                elif cur_sum < target:
                    second_idx += 1
                else:
                    third_idx -= 1

                while second_idx > first_idx + 1 and second_idx < third_idx and nums[second_idx] == nums[
                    second_idx - 1]:  # 如果当前值和上一个值一样，那么不需要重新
                    second_idx += 1

                while third_idx > second_idx and third_idx < (count - 1) and nums[third_idx] == nums[third_idx + 1]:
                    third_idx -= 1

        return res


su = SetUtils()
nums, target = [randint(-9, 9) for _ in range(10)], randint(-18, 18)
# nums, target = [9, 6, 8, 6, 2, 1, -2, 3, -9, 9], 7
print(nums, target)
print(su.two_sums(nums, target))
print(su.two_sums_idx(nums, target))
print(su.three_sums(nums, target))
print(su.three_sums_v2(nums, target))
