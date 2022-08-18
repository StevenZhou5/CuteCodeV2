# 224. 基本计算器
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数


class Solution:
    def calculate(self, s: str) -> int:
        # 个人解法：所有元素入栈法
        # stack = []
        # no_opt_chr = set(['(','-','+'])
        # for c in s:
        #     if c == ' ': # 空字符串
        #         continue

        #     if c in no_opt_chr: #'(','-','+' 这三个直接入栈
        #         stack.append(c)
        #         continue

        #     if c == ')': # ')' 一定要找到第一个匹配的左边括号
        #         inner_num = 0
        #         while True:
        #             last_c = stack.pop()
        #             if last_c == '(':
        #                 if stack: # 如果stack不为空，那么(前必定有符号，要根据符号修正最终括号内的值
        #                     if stack[-1] == '+':
        #                         stack.pop()
        #                     elif stack[-1] == '-':
        #                         stack.pop()
        #                         inner_num = -inner_num
        #                 break
        #             # print(last_c)
        #             inner_num += last_c
        #         stack.append(inner_num)
        #     else: # 数字处理，数字前面有可能是 '+' 、'-' 、'(' 、或者数字
        #         cur_num = ord(c) - ord('0')
        #         if stack and stack[-1] != '(':
        #             # print("1",stack,cur_num)
        #             last_c = stack.pop()
        #             # print("2",stack,cur_num)
        #             if last_c == '+': # 如果是+号，只需要将将+号移除栈即可
        #                 pass
        #             elif last_c == '-': # 如果是-号，需要将num的值取负
        #                 cur_num = -cur_num
        #             elif last_c > 0:
        #                 cur_num = last_c * 10 + cur_num
        #             elif last_c < 0:
        #                 cur_num = last_c * 10 - cur_num # 如果是前一个数是负数，那么新的cur_num要作为负数的个位数，需要减掉
        #         stack.append(cur_num)

        # # print(stack)
        # return sum(stack)

        # 符号栈：只记录符号栈
        opt_stack = [1]
        sign = 1
        res = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':  # 如果是正号，符号与当前层括号的操作符号保持一致
                i += 1
                sign = opt_stack[-1]
            elif s[i] == '-':  # 如果是符号，符号与当前层括号的操作符号取负
                i += 1
                sign = -opt_stack[-1]
            elif s[i] == '(':  # 左括号时，符号入栈
                i += 1
                opt_stack.append(sign)
            elif s[i] == ')':  # 右括号时，符号出栈
                i += 1
                opt_stack.pop()
            else:  # s[i] 为数字
                num = 0
                while i < n and s[i].isdigit():  # 所有位数补齐，算出数字的
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                # print(num,res)
                res += (sign * num)

        return res
