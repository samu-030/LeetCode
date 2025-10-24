class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        arr1 = []

        i = 0
        while i < len(nums):
            alice = nums[i]
            bob = nums[i+1]
            arr1.append(bob)
            arr1.append(alice)
            i += 2

        return arr1