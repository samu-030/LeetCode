class Solution(object):
    def countDigitOccurrences(self, nums, digit):

        count = 0

        for num in nums:
            
            while num > 0:
                rem = num % 10
                if rem == digit:
                    count += 1
                num = num//10

        return count

        

#solution 1:

"""count = 0
target = str(digit)

for i in nums:
    for ch in str(i):
        if ch == target:
            count += 1
return count"""

#Rough workout:
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