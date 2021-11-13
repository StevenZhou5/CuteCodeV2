# 739. 每日温度
# 请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
# 示例 1:
#
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 示例 2:
#
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 示例 3:
#
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
#
# 提示：
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution():
    def get_all_next(self, temperatures):
        if not temperatures:
            return []
        res = [0] * len(temperatures)
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:  # 更新所有比当前温度小的天
                cur_idx = stack.pop()
                res[cur_idx] = idx - cur_idx
            stack.append(idx)
        return res


solu = Solution()
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures = [30, 40, 50, 60]
temperatures = [30, 60, 90]
print("res:", solu.get_all_next(temperatures))
