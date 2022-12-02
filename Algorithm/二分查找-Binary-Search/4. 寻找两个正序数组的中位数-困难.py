# 4. 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
# 提示：
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        # 二分查找
        # 时间复杂度：O(log(m + n))
        # 空间复杂度：O(1)
        m, n = len(nums1), len(nums2)

        def recursion(s1, e1, s2, e2, k):
            # print(s1, e1, s2, e2, k)
            if s1 > e1:  # 数组1已经遍历完了
                return nums2[s2 + k]
            if s2 > e2:  # 数组2已经遍历完了
                return nums1[s1 + k]
            if k == 0:
                return min(nums1[s1], nums2[s2])
            mid_idx = min((k - 1) >> 1, e1 - s1, e2 - s2)
            if nums1[s1 + mid_idx] <= nums2[s2 + mid_idx]:
                return recursion(s1 + mid_idx + 1, e1, s2, e2, k - mid_idx - 1)
            else:
                return recursion(s1, e1, s2 + mid_idx + 1, e2, k - mid_idx - 1)

        if (m + n) & 1 == 1:  # 奇数只要中间数
            return recursion(0, m - 1, 0, n - 1, (m + n) >> 1)
        else:
            return 0.5 * (recursion(0, m - 1, 0, n - 1, (m + n - 1) >> 1) + recursion(0, m - 1, 0, n - 1, (m + n) >> 1))
