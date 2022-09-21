# 338. 比特位计数
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 示例 2：
#
# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
# 提示：
#
# 0 <= n <= 105
#
#
# 进阶：
#
# 很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
# 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）

class Solution:
    def countBits(self, n: int) -> List[int]:
        # 位运算：时间复杂度 O(nlogn); 空间复杂度O(1)
        # res = []
        # for i in range(n + 1):
        #     count = 0
        #     while i:
        #         i &= i - 1
        #         count += 1
        #     res.append(count)
        # return res

        # 位运算 + 动态规划：时间复杂度O(n); 空间复杂度O(1)
        res = [0]
        for i in range(1, n + 1):
            res.append(
                res[i & (i - 1)] + 1)  # i & (i - 1) 是去掉i的最后一个1， 那么i的二进制为 一定只比 i & (i - 1) 多一个 1， 且 i & (i - 1) 一定比 i小；
        return res
