class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        target = str(digit)

        for i in nums:
            for ch in str(i):
                if ch == target:
                    count += 1
        return count
