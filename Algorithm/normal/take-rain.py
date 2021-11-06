class Solution(object):
    def __init__(self):
        pass

    def max_continer(self, nums):
        if not nums:
            return 0
        res = 0
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx < right_idx:
            if nums[left_idx] <= nums[right_idx]:
                cur_val = nums[left_idx] * (right_idx - left_idx)
                left_idx += 1

            else:
                cur_val = nums[right_idx] * (right_idx - left_idx)
                right_idx -= 1

            if cur_val > res:
                res = cur_val
        return res

    def take_rain(self, nums):
        if not nums:
            return 0
        cnt = len(nums)
        from collections import deque
        left_to_right = deque()
        left_to_right.append(nums[0])
        for i in range(1, cnt):
            left_to_right.append(nums[i] if nums[i] > left_to_right[-1] else left_to_right[-1])
        right_to_left = deque()
        right_to_left.append(nums[cnt - 1])
        for i in range(cnt - 2, -1, -1):
            right_to_left.appendleft(nums[i] if nums[i] > right_to_left[0] else right_to_left[0])

        print(left_to_right, right_to_left)

        res = 0
        for i in range(cnt):
            res += min(left_to_right[i], right_to_left[i]) - nums[i]

        return res


from random import randint

nums = [randint(0, 10) for _ in range(10)]
print(nums)
solu = Solution()
print("max_continer:", solu.max_continer(nums))
print("take rain:", solu.take_rain(nums))
