class Solution(object):
    def xorOperation(self, n, start):
        
        xorSum = 0
        for i in range(n):
            res = start + 2 * i
            xorSum ^= res
            

        return xorSum

