# 93. 复原 IP 地址
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按 任何 顺序返回答案。
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
#
#
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
# 提示：
#
# 0 <= s.length <= 3000
# s 仅由数字组成

class Solution():
    def get_all_valid_ip(self, s):
        if not s:
            return []
        res = []

        def is_valid(cur_ips):
            if not cur_ips or (len(cur_ips) > 1 and cur_ips[0] == '0'):
                return False

            return 0 <= int(cur_ips) <= 255

        def get_all(left_s, used_point, tar_str):
            if used_point == 3:
                if is_valid(left_s):
                    res.append(tar_str[1:] + "." + left_s)
                return
            for i in range(min(3, len(left_s))):
                cur_s = left_s[:i + 1]
                if is_valid(cur_s):  # is_valid
                    get_all(left_s[i + 1:], used_point + 1, tar_str + '.' + cur_s)

        get_all(s, 0, "")
        return res


solu = Solution()
s_list = ["25525511135", "0000", "1111", "010010", "101023"]
for s in s_list:
    print("res:", solu.get_all_valid_ip(s))
