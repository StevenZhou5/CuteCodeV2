# 816. 模糊坐标
# 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。
#
# 原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
#
# 最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
#
#
#
# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释:
# 0.0, 00, 0001 或 00.01 是不被允许的。
# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释:
# 1.0 是不被允许的。
#
#
# 提示:
#
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # 枚举 + 剪枝
        res = []
        n = len(s)

        def is_valid(start, end, split):
            if (s[start] == '0' and (split - start > 0)) or (end > start and s[end] == '0'):
                return False
            return True

        for i in range(1, n - 2):  # 确定','号的位置
            # print(i)
            valid_list1 = []
            if s[1] != '0' or i == 1:
                valid_list1.append(s[1: i + 1])
            for j in range(1, i):  # 找到所有合理的坐标1的表示,风格符只能放在第 1个到第i-1个字符后面
                if is_valid(1, i, j):
                    valid_list1.append(s[1: j + 1] + '.' + s[j + 1: i + 1])
                else:
                    break  # 只要有一个位置不合理，后面的都不合理

            if not valid_list1:  # 如果没有合理的坐标1，不用构造坐标2
                continue
                # print(valid_list1)
            valid_list2 = []
            if s[i + 1] != '0' or (i == n - 3):
                valid_list2.append(s[i + 1: n - 1])
            for k in range(i + 1, n - 2):  # 找到所有合理的坐标2的表示
                # print(i + 1, n - 1, k)
                if is_valid(i + 1, n - 2, k):
                    valid_list2.append(s[i + 1: k + 1] + '.' + s[k + 1: n - 1])
                else:
                    break  # 只要第一次遇见位置不合理的，后面的位置都不会合理

            if not valid_list2:  # 如果没有合理的坐标2，继续探索下一个分割点
                continue

            for i in range(len(valid_list1)):
                for j in range(len(valid_list2)):
                    res.append('(' + valid_list1[i] + ', ' + valid_list2[j] + ')')

        return res
