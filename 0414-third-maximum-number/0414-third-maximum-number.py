class Solution(object):
    def thirdMax(self, nums):
        nums = sorted(set(nums))
        return nums[-3] if len(nums) >= 3 else nums[-1]