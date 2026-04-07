class Solution(object):
    def majorityElement(self, nums):

        n = len(nums)

        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0

        for i in nums:

            if ele1 == i:
                cnt1 += 1
            elif ele2 == i:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = i
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = i
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        res = 0
        cnt1, cnt2 = 0, 0

        for i in nums:
            if ele1 == i:
                cnt1 += 1
            if ele2 == i:
                cnt2 += 1

        if cnt1 > (n/2):
            res = ele1
        if cnt2 > (n/2) and ele1 != ele2:
            res = ele2

        return res



