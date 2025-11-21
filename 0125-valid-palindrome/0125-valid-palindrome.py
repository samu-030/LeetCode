class Solution(object):
    def isPalindrome(self, s):
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()

        return string == string[::-1]

    
