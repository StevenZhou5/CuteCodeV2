# 301. 删除无效的括号
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。
#
#
#
# 示例 1：
#
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
# 示例 2：
#
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
# 示例 3：
#
# 输入：s = ")("
# 输出：[""]
#
#
# 提示：
#
# 1 <= s.length <= 25
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 递归 + 回溯 + 剪枝
        # 时间复杂度：O(n * 2^n) 没删除一个字符有n种组合
        # 空间复杂度：O(2 ^ n) 递归深度
        # max_len = 0
        # n = len(s)
        # left_cnt = 0
        # for i in range(n):
        #     if s[i] == '(':
        #         left_cnt += 1
        #         continue
        #     elif s[i] == ')':
        #         if left_cnt > 0:
        #             left_cnt -= 1
        #             max_len += 2
        #     else:
        #         max_len += 1

        # # print(max_len)
        # res = set()
        # def recursion(idx, left_cnt, right_cnt, cur_str):
        #     visted_key = cur_str + str(idx)
        #     # print(cur_str)
        #     # 递归终止条件
        #     if len(cur_str) == max_len: # 如果已经是最大长度，判断是否合法, 这个一定要在越界前判断
        #         if left_cnt == right_cnt: # 合法添加到最终结果中
        #             res.add(cur_str)
        #         return
        #     if idx >= n: # 如果越界返回
        #         return
        #     if s[idx] != '(' and s[idx] != ')': # 剪枝：如果是字母一定要选
        #         recursion(idx + 1, left_cnt, right_cnt, cur_str + s[idx])
        #         return

        #     recursion(idx + 1, left_cnt, right_cnt, cur_str) # 任何时候都可以既不选'(' 也不选 ')'

        #     if s[idx] == '(': # 任何时候都可以直接添加'('
        #         recursion(idx + 1, left_cnt + 1, right_cnt, cur_str + s[idx])
        #     if left_cnt > right_cnt and  s[idx] == ')': # 只有左括号比右括号多的时候才能添加')'
        #         recursion(idx + 1, left_cnt, right_cnt + 1, cur_str + s[idx])

        # recursion(0, 0, 0, "")
        # return list(res)

        # 递归 + 回溯 + 剪枝 + 缓存 : 空间换时间
        # 时间复杂度：O(n * 2^n) 没删除一个字符有n种组合
        # 空间复杂度：O(2 ^ n) 递归深度
        max_len = 0
        n = len(s)
        left_cnt = 0
        for i in range(n):
            if s[i] == '(':
                left_cnt += 1
                continue
            elif s[i] == ')':
                if left_cnt > 0:
                    left_cnt -= 1
                    max_len += 2
            else:
                max_len += 1

        # print(max_len)
        res = set()
        visted_set = set()  # 缓存已经处理过的情况

        def recursion(idx, left_cnt, right_cnt, cur_str):
            visted_key = cur_str + str(idx)
            if visted_key in visted_set:
                return
            visted_set.add(visted_key)
            # print(cur_str)
            # 递归终止条件
            if len(cur_str) == max_len:  # 如果已经是最大长度，判断是否合法, 这个一定要在越界前判断
                if left_cnt == right_cnt:  # 合法添加到最终结果中
                    res.add(cur_str)
                return
            if idx >= n:  # 如果越界返回
                return
            if s[idx] != '(' and s[idx] != ')':  # 剪枝：如果是字母一定要选
                recursion(idx + 1, left_cnt, right_cnt, cur_str + s[idx])
                return

            recursion(idx + 1, left_cnt, right_cnt, cur_str)  # 任何时候都可以既不选'(' 也不选 ')'

            if s[idx] == '(':  # 任何时候都可以直接添加'('
                recursion(idx + 1, left_cnt + 1, right_cnt, cur_str + s[idx])
            if left_cnt > right_cnt and s[idx] == ')':  # 只有左括号比右括号多的时候才能添加')'
                recursion(idx + 1, left_cnt, right_cnt + 1, cur_str + s[idx])

        recursion(0, 0, 0, "")
        return list(res)
