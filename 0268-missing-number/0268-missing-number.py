class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor_all = 0
        for i in range(n+1):
            xor_all ^= i
        for num in nums:
            xor_all ^= num

        return xor_all