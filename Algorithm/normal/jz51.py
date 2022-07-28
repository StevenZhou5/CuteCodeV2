# 剑指 Offer 51. 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#
#
# 示例 1:
#
# 输入: [7,5,6,4]
# 输出: 5
#
#
# 限制：
#
# 0 <= 数组长度 <= 50000
#
# 通过次数106,301提交次数219,907


class Solution():
    def get_count(self, nums):
        if not nums or len(nums) < 2:
            return 0
        self.res = 0

        def merge_two(nums_left, nums_right):
            print("nums_left:", nums_left, "nums_right:", nums_right)
            if not nums_left or not nums_right:
                return nums_left + nums_right
            cur_res = []
            mid_left = len(nums_left) >> 1
            nums_left = merge_two(nums_left[:mid_left].copy(), nums_left[mid_left:].copy())
            mid_right = len(nums_right) >> 1
            nums_right = merge_two(nums_right[:mid_right].copy(), nums_right[mid_right:].copy())
            print("nums_left2:", nums_left, "nums_right2:", nums_right)
            while nums_left and nums_right:
                if nums_left[0] > nums_right[0]:
                    self.res += len(nums_left)  # 此时所有左边列表中的元素都比此时右边第一个值大，构成len(nums_left)对逆序对
                    cur_res.append(nums_right.pop(0))
                else:  # 相等的时候左边先进
                    cur_res.append(nums_left.pop(0))
            # 如果左边为空，那么右边都是大的，没有逆序对；
            # 如果右边为空，那么在循环的时候都计算过了，所以也不需要额外计算
            if not nums_left:
                cur_res += nums_right
            else:
                cur_res += nums_left
            return cur_res

        mid = len(nums) >> 1
        nums = merge_two(nums[:mid].copy(), nums[mid:].copy())
        print("sorted_nums:", nums)
        return self.res


solu = Solution()

# nums = [randint(-5, 5) for _ in range(randint(0, 5))]
nums = [7, 5, 6, 4, 8, 1]
print("nums:", nums)
print("res:", solu.get_count(nums))
