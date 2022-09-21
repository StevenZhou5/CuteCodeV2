# 67. 二进制求和
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
# 提示：
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 模型位远算：时间复杂度O(n) n位a、b中的最大长度；空间复杂度O(1);
        cur_state = 0
        res = ""
        while a or b or cur_state:  # 这样做的好处是不需要啊额外处理最后一位进位
            cur_a = int(a[-1]) if a else 0
            cur_b = int(b[-1]) if b else 0
            sum_val = cur_a + cur_b + cur_state
            if sum_val == 0:
                res = '0' + res
                cur_state = 0
            elif sum_val == 1:
                res = '1' + res
                cur_state = 0
            elif sum_val == 2:
                res = '0' + res
                cur_state = 1
            else:
                res = '1' + res
                cur_state = 1
            a = a[:-1]
            b = b[:-1]
        return res
