class Solution(object):
    def differenceOfSum(self, nums):
        el_sum = di_sum = 0
        for i in nums:
            el_sum += i
            while i > 0:
                di_sum += i % 10
                i //= 10

        return abs(el_sum - di_sum)