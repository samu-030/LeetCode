class Solution(object):
    def signFunc(self, x):
        if x > 0 :
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def arraySign(self, nums):
        res = 1
        for i in nums:
            res *= i

        return self.signFunc(res)

