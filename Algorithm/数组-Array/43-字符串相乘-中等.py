# 43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
#
#
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#
# 提示：
#
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 模拟运算
        # 时间复杂度 O((m + (m +n)) * n) = O(n ^ 2 + m * n),m 是nmms1 的长度，n 是nums2的长度，外层循环n次，内层乘法操作 时间复杂度O（m）, 加法操作时间复杂度O（m + n）
        # 空间复杂度 O(m + n) 存储中间状态的字符串长度
        # if num1 == '0' or num2 == '0':
        #     return "0"

        # def str_multiply_x(s, x): # 执行字符串s 与 单个数字x相乘
        #     cur_res = ""
        #     cur_pre = 0 # 进位
        #     for i in range(len(s) - 1, -1, -1):
        #         tmp_val = int(s[i]) * x + cur_pre
        #         cur_res = str(tmp_val % 10 ) + cur_res
        #         cur_pre = tmp_val // 10
        #     return str(cur_pre) + cur_res if cur_pre > 0 else cur_res

        # def add_str(s1, s2): # 执行两个数字字符串相加
        #     cur_res = ""
        #     cur_pre = 0
        #     idx = 0
        #     m, n = len(s1), len(s2)
        #     while idx < m or idx < n or cur_pre: # 只要有一个地方还有值就需要继续加下去
        #         tmp_val = (int(s1[m - idx - 1]) if idx < m else 0) + (int(s2[n - idx - 1]) if idx < n else 0)  + cur_pre
        #         # print(str(tmp_val % 10) + cur_res, tmp_val, cur_res)
        #         cur_res = str(tmp_val % 10) + cur_res
        #         cur_pre = tmp_val // 10
        #         idx += 1
        #     return cur_res

        # res = ""
        # for i in range(len(num2)):
        #     res = add_str(res + "0", str_multiply_x(num1, int(num2[i])))

        # return res

        # 转换为数组
        # 时间复杂度：O(m * n) , 利用数组暂存每一位的总和，时间复杂度O(m * n), 在对每一位的和从最小位开始进行进位操作，时间复杂度O(m + n), 所以总体时间复杂度O(m * n)
        # 空间复杂度：O(m + n) , 数据的长度为 m + n
        if num1 == '0' or num2 == '0':
            return "0"
        m, n = len(num1), len(num2)
        arr_res = [0] * (m + n)  # 最多的位数
        for i in range(m):
            for j in range(n):
                idx = i + j + 1
                arr_res[idx] += int(num1[i]) * int(num2[j])
        res = ""
        for i in range(m + n - 1, 0, -1):
            arr_res[i - 1] += arr_res[i] // 10
            arr_res[i] = arr_res[i] % 10
            res = str(arr_res[i]) + res

        return (str(arr_res[0]) + res) if arr_res[0] > 0 else res
