# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
# 提示：
#
# 1 <= s.length <= 30
# s 由小写英文字母、数字和方括号 '[]' 组成
# s 保证是一个 有效 的输入。
# s 中所有整数的取值范围为 [1, 300]

class Solution:
    def decodeString(self, s: str) -> str:
        # 堆栈法
        if not s:
            return ""
        n = len(s)
        stack_res = []
        i = 0
        while i < n:
            # print(stack_res)
            if s[i].isdigit(): # 如果是数字，需要将当前数字的所有数字位解析完，此时内存循环的i与外层循环的i共用
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                stack_res.append(num)
            elif s[i] == ']': # 如果当前是']'，那么要解析到匹配的'['以及括号前面的数字
                cur_str = stack_res.pop()
                while stack_res and stack_res[-1] != '[': # 将多层括号字符串相加
                    cur_str = stack_res.pop() + cur_str
                stack_res.pop() # 移除左括号
                cur_repeat_str = cur_str * stack_res.pop()
                stack_res.append(cur_repeat_str)
                i += 1
            else: # 当为普通字符 和 '[' 时，不用额外处理
                stack_res.append(s[i])
                i += 1 # 注意i + 1操作一定要在append之后


        # print(stack_res)
        return ''.join(stack_res)
