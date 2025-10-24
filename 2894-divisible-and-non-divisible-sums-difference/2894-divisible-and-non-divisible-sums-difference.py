class Solution(object):
    def differenceOfSums(self, n, m):
        sum1, sum2 = 0, 0
        for i in range(1, n+1):
            if(i % m == 0):
                sum1 += i
            else:
                sum2 += i
        res = (sum2 - sum1)

        return res
