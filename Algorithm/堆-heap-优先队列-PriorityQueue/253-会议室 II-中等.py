# 253. 会议室 II
# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 示例 2：
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
#
#
# 提示：
#
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        # 有序化
        # 时间复杂度：O(n * log n)
        # 空间复杂度：O(n)
        # n = len(intervals)
        # start_list = sorted([intervals[i][0] for i in range(n)])
        # end_list = sorted([intervals[i][1] for i in range(n)])

        # res = 0
        # p_s, p_e = 0, 0
        # while p_s < n:
        #     if start_list[p_s] < end_list[p_e]: # 在当前会议开始时，并没有结束的会议，需要一个新的会议室
        #         res += 1
        #         p_s += 1
        #     else: # 当前会议可以接在一个结束的会议后
        #         p_s += 1
        #         p_e += 1
        # return res

        # 排序 + 优先队列 + 贪心
        # 时间复杂度：O(n * log(n)) 排序时间复杂度O(n * log n),最差情况下需要n间会议室
        # 空间复杂度：O(n) 最坏情况下需要n间会议室
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        import heapq
        min_end_pq = [intervals[0][1]]
        res = 1
        for i in range(1, n):
            # print(min_end_pq)
            if intervals[i][0] < min_end_pq[0]:  # 如果跟结束时间最早的会议室都冲突了，需要加一间会议室
                res += 1
                heapq.heappush(min_end_pq, intervals[i][1])
            else:  # 贪心： 可以接在结束时间最早的会议室前面开
                heapq.heapreplace(min_end_pq, intervals[i][1])

        return res
