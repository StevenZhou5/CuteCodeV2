# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
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

class Solution():

    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda item: item[0])  # 注意，这里一定要用下届排序
        print("sorted intervals:", intervals)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1] = [min(intervals[i][0], res[-1][0]), max(intervals[i][1], res[-1][1])]
        return res


from random import randint

intervals = [[i, i + randint(1, 10)] for i in [randint(-10, 10) for _ in range(randint(0, 10))]]
# intervals = [[-10, 10], [-5, 8], [-8, -7]]
print("intervals:", intervals)
solu = Solution()
print("res:", solu.merge(intervals))
