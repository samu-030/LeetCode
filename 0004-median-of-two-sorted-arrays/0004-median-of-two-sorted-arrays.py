class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        sorted_nums = sorted(nums1 + nums2)

        n = len(sorted)
        mid = n//2

        if n%2 == 0:
            return (sorted_nums[mid-1] + sorted_nums[mid]) / 2.0

        else:
            return sorted_nums(mid)
        
        
        
        
        '''
        for i in nums2:
            nums1.append(i)

        nums1.sort()
        n = len(nums1)
        mid = n//2

        if n%2 == 0:
            res = nums1[mid-1] + nums1[mid]
            return res/2.0

        else:
            return nums1[mid]

        '''