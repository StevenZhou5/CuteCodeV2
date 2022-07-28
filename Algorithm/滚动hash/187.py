# 187. 重复的DNA序列
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
#
#
#
# 示例 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#
#
# 提示：
#
# 0 <= s.length <= 105
# s[i] 为 'A'、'C'、'G' 或 'T'


class Solution():

    def get_all_sub_str(self, s):
        n = len(s)
        if n <= 10:
            return []

        # 滚动hash
        base = 5
        mod = 999983
        hash_map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        all_sub_set = set()
        res = []
        cur_rk_val = 0
        for i in range(10):
            cur_rk_val = (((cur_rk_val * base) % mod) + hash_map[s[i]]) % mod
        all_sub_set.add(cur_rk_val)

        # 因为长度限制为10,所以可以提前计算好要减去的mod值
        sub_mod = base % mod
        for _ in range(9):
            sub_mod = (sub_mod * base) % mod

        for i in range(10, n):
            cur_rk_val = cur_rk_val - (hash_map[s[i-10]] * sub_mod)%mod

        return
