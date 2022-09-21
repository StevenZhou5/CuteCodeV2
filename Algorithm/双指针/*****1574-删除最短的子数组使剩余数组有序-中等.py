# 1574. 删除最短的子数组使剩余数组有序
# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
#
# 一个子数组指的是原数组中连续的一个子序列。
#
# 请你返回满足题目要求的最短子数组的长度。
#
#
#
# 示例 1：
#
# 输入：arr = [1,2,3,10,4,2,3,5]
# 输出：3
# 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
# 另一个正确的解为删除子数组 [3,10,4] 。
# 示例 2：
#
# 输入：arr = [5,4,3,2,1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
# 示例 3：
#
# 输入：arr = [1,2,3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。
# 示例 4：
#
# 输入：arr = [1]
# 输出：0
#
#
# 提示：
#
# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9

class Solution:
    def findLengthOfShortestSubarray(self, arr: [int]) -> int:
        # 双指针 + 二分查找： 先找出左边有序 和 右边有序区间； 然后依次扩充左(或右)区间，用二分查找去另一个区间找满足要求的位置，然后对比此时删除段的长度，更新最终结果
        # 时间复杂度：O(n * log n)，查找左右区间 O(n) 的复杂度；设左段长度 n1, 右段长度 n2，遍历 + 二分查找需要 min(O(n1 * log n2), O(n2 * log n1)) 的时间复杂度，所以真题时间复杂度为O(n * log n)
        # 空间复杂度：O(1)
        # l, r = -1, -1 # [0,l]和 [r,n-1] 单调递增，
        # n = len(arr)
        # # 找出左边单调递增区间
        # for i in range(1,n):
        #     if arr[i] < arr[i - 1]:
        #         l = i - 1
        #         break
        # # 找出右边单调递增区间
        # for j in range(n - 2, -1, -1):
        #     if arr[j] > arr[j + 1]:
        #         r = j + 1
        #         break

        # # print(l, r)
        # if l == -1: # 整个数组完全单调，
        #     return 0
        # # 优化，左右两边那边短遍历那边，二分查找长的那边
        # res = min(r, n - 1 - l) # 初始只选整个右区间有序, 那么r前面的所有数都要移除; 或者只选左区间，整个右区间都要移除
        # if l <= (n - 1 - r): # 左边短
        #     for i in range(l + 1):
        #         target = arr[i]
        #         # 通过二分查找，找到右区间第一个>= 目标的位置
        #         # 左开右开，向下取整，左定右定，相邻终止
        #         r_l, r_r = r - 1, n # 左开右开
        #         while r_l + 1 < r_r:
        #             mid = (r_r + r_l) >> 1 # 注意这里不能用 r_l + ((r_r - r_l) >> 1) 的方式，会越界，因为我们的r_l 和 r_r 都是左开右开的
        #             if arr[mid] < target:
        #                 r_l = mid
        #             else:
        #                 r_r = mid
        #         # print(target, r_r, arr[r_r] if r_r < n else None)
        #         if r_r != n: # 说明有比target大的数
        #             res = min(res, r_r - i - 1)
        #         else: # 当前值已经在右边界找不到比它大的值了，那么就直接跳出循环即可
        #             break
        # else:
        #     for j in range(n-1, r - 1, -1):
        #         target = arr[j]
        #         l_l, l_r = -1, l + 1 # 左开右开
        #         while l_l + 1 < l_r:
        #             mid = (l_l + l_r) >> 1
        #             if arr[mid] > target:
        #                 l_r = mid
        #             else:
        #                 l_l = mid
        #         if l_r != 0:
        #             res = min(res, j - l_l - 1 )
        #         else:
        #             break
        # return res

        # 双指针滑动 ： 固定一侧指针每次滑动一个位置，另外一层指针滑动找到满足条件的位置，因为两侧都有单调性，所以已经看过的位置不需要再后续重复看；时间复杂度优化到O(n)
        # 时间复杂度：O(n),找到左右边界时间复杂度O(n), 左右指针移动时间复杂度O(n);
        # 空间复杂度：O(1)
        # n = len(arr)
        # l, r  = -1, -1
        # for i in range(1,n):
        #     if arr[i] < arr[i - 1]:
        #         l = i - 1
        #         break

        # for j in range(n - 2, -1, -1):
        #     if arr[j] > arr[j + 1]:
        #         r = j + 1
        #         break
        # if l == -1:
        #     return 0

        # res = min(n - 1 - l, r)
        # for i in range(l + 1):
        #     while r < n and arr[r] < arr[i]:
        #         r += 1
        #     if r > n - 1:
        #         break
        #     res = min(res, r - i - 1)
        # return res

        # 双指针滑动 + 二分查找 (终极解法)：在解法二的基础上进一步优化，使用二分查找不断更新左短的右指针 和 右段的左指针
        # 时间复杂：O(n),查找左右边界，时间复杂度O(n); 更新左右边界都是二分查找，时间复杂度为O(log n1) + O(log n2) <= O(log n); 所以总体时间复杂度O(n)
        # 空间复杂度：O(1)
        n = len(arr)
        l, r = -1, -1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                l = i - 1
                break

        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                r = j + 1
                break

        if l == -1:  # 整个数组单调递增
            return 0
        # print(l, r)
        res = min(n - 1 - l, r)
        l_l = 0  # 左段二分找出从左段左边界从第一个元素开始
        r_l = r  # 右段二分查找从右段左边界也从第一个元素开发室
        while l_l <= l and r_l <= n - 1:
            if arr[l_l] <= arr[r_l]:  # 左边的最大值小于右边的最小值，左段边界右移
                target = arr[r_l]
                cur_l, cur_r = l_l - 1, l + 1
                while cur_l + 1 < cur_r:
                    mid = (cur_l + cur_r) >> 1
                    if arr[mid] > target:
                        cur_r = mid
                    else:
                        cur_l = mid
                if cur_l == l_l - 1:  # 在左边找不到比右边小的值了，直接brake
                    break
                # print(cur_l, r)
                res = min(res, r_l - cur_l - 1)
                l_l = cur_l + 1  # arr[cur_l] 一定是<= arr[r_l], 而 cur_l + 1 一定大于 arr[r_l], 所以需要 + 1，下一次一定更新右段
            else:
                target = arr[l_l]
                cur_l, cur_r = r_l - 1, n
                while cur_l + 1 < cur_r:
                    mid = (cur_l + cur_r) >> 1
                    if arr[mid] < target:
                        cur_l = mid
                    else:
                        cur_r = mid
                if cur_r == n:  # 在右边找不到比左边大的值了
                    break
                res = min(res, cur_r - l_l - 1)
                r_l = cur_r  # 因为arr[cur_r] 一定>= target, 下次一定会更新左段，所以不用 + 1

        return res
