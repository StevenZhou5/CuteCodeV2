# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
# 提示：
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        # 排序：
        # 时间复杂度：O(n * log n)，其中 n 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(n * log n)。
        # 空间复杂度：O(1)
        intervals.sort(key=lambda x: x[0])
        res = []
        for start_i, end_i in intervals:
            if not res or start_i > res[-1][1]:  # 如果当前start_i 比最后一个区间的右边界大，那么把新区间加入
                res.append([start_i, end_i])
            else:  # 否侧尝试更新右边界
                res[-1][1] = max(res[-1][1], end_i)  # 右边界需要找最大值
        return res
