class Solution(object):
    def isPalindrome(self, x):
    
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        original_x = x
        
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        
        if (-2**31 > x) or (x < 2**31):
            if (sign * rev) == original_x:
                return True
            else:
                return False

        return True
        