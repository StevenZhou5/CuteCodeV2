# 1124. 表现良好的最长时间段
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
# 请你返回「表现良好时间段」的最大长度。
#
#
#
# 示例 1：
#
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
#
# 输入：hours = [6,6,6]
# 输出：0
#
#
# 提示：
#
# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16
class Solution:
    def longestWPI(self, hours: [int]) -> int:
        # 前缀和 + 记录最早出现前缀和
        # 时间复杂度：O(n),只遍历一次；
        # 空间复杂度：O(n), 存储前缀和map；
        # n = len(hours)
        # res = 0
        # pre_sum = 0
        # pre_sum_idx_map = {0: -1}
        # for i in range(n):
        #     if hours[i] > 8:
        #         pre_sum += 1
        #     else:
        #         pre_sum -= 1
        #
        #     if pre_sum not in pre_sum_idx_map:
        #         pre_sum_idx_map[pre_sum] = i # 记录最早出现的pre_sum
        #
        #     if pre_sum > 0:
        #         res = i + 1
        #     elif pre_sum - 1 in pre_sum_idx_map:
        #         res = max(res, i - pre_sum_idx_map[pre_sum - 1]) # 假设pre_sum = -1， 那么pre_sum - 1 = -2, 会不会先出先出现-3，在出现-2呢？答案是不会，因为这个和每次最多 + 1或 -1，所以-3 第一个-3 一定在第一个 -2 的右边，所以i - pre_sum_idx_map[pre_sum - 1] 就能保证长度最长；
        #
        # return res

        # 单调栈
        # 时间复杂度：O(n) 3次循环遍历，总共3n
        # 空间复杂度：O(n) 需要存储pre_sum 和单调递减栈
        n = len(hours)
        pre_sums = [0]  # 0个元素相加
        for i in range(1, n + 1):
            pre_sums.append(pre_sums[-1] + (1 if hours[i - 1] > 8 else -1))
        # print(pre_sums)
        res = 0
        stack = [0]  # pre_sum单调递减的索引
        for i in range(1, n + 1):
            if pre_sums[i] < pre_sums[stack[-1]]:
                stack.append(i)
        idx = n
        while idx > 0:  # 从右往左遍历
            while stack and pre_sums[idx] > pre_sums[stack[-1]]:  # 满足条件说明 stack[-1] 到 idx 的和是大于 1 的
                res = max(res, idx - stack[-1])  # 如果idx 比 stack[-1] 小也不用担心，因为会后面会移除stack[-1]
                stack.pop()  # 虽然pre_sums[idx] 比  pre_sums[stack[-1]] 大，但是不一定能保证比pre_sums[stack[-2]] 大，因为stack的pre_sum是单调递减的，所以需要移除-1，继续看是否满足
            idx -= 1

        return res
