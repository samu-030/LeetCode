class Solution(object):
    def rotate(self, nums, k):
        
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n-1)

        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, st, end):

        while st < end:

            nums[st], nums[end] = nums[end], nums[st]

            st += 1
            end -= 1
    
        