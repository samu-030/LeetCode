class Solution(object):
    def firstMatchingIndex(self, s):
        n = len(s)

        left = 0
        right = n-1

        while (left <= right):

            if s[left] == s[right]:
                return left

            left += 1
            right -= 1

        return -1
        '''
        n = len(s)

        if n < 2:
            return 0

        for i in range (n//2):
            if s[i] == s[n-1-i]:
                return i

        return -1'''


        