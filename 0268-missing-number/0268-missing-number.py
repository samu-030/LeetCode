class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        ex_sum = n * (n + 1) // 2
        act_sum = sum(nums)

        return ex_sum - act_sum
