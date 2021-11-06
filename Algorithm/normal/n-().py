class Solution(object):

    def __init__(self):
        self.res = []

    def get_res(self, n):
        self.res = []
        self.get_(0, 0, "", n)
        return self.res

    def get_(self, left_used, right_used, target, n):
        if left_used == right_used == n:
            self.res.append(target)
            return

        if left_used < n:
            self.get_(left_used + 1, right_used, target + "(", n)
        if right_used < n and right_used < left_used:
            self.get_(left_used, right_used + 1, target + ")", n)


sou = Solution()
print(sou.get_res(3))
