class Solution(object):
    def isPalindrome(self, s):
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()

        if string == string[::-1]:
            return True

        return False
