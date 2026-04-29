class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        target = str(digit)

        for i in nums:
            for ch in str(i):
                if ch == target:
                    count += 1
        return count

        '''for i in nums:
            if i > 9:
                rem = i % 10
                i = i // 10

                if rem == digit:
                    count += 1

            if i == digit:
                count += 1

        return count
        '''