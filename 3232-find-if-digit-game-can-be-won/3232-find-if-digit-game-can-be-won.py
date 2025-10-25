class Solution(object):
    def canAliceWin(self, nums):
        sum_A, sum_B = 0, 0
        for i in nums:
            if i <= 9:
                sum_A += i
            else:
                sum_B += i

        if sum_A != sum_B:
            return True

        return False
    