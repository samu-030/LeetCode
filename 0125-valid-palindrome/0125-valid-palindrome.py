class Solution(object):
    def isPalindrome(self, s):
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()

        s_rev = string[::-1]

        if s_rev == string:
            return True

        return False
