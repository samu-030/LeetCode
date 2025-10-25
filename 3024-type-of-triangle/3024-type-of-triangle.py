class Solution(object):
    def triangleType(self, nums):
        a, b, c = nums
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "none"
        elif (a == b) and (a == c):
            return "equilateral"
        elif (a == b) or (a == c) or (b == c):
            return "isosceles"
        else:
            return "scalene"
        


        