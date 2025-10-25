class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        rev_string = ""
        word = s.split()
        for i in word:
            rev_string = i + " " + rev_string 

        return rev_string.strip()