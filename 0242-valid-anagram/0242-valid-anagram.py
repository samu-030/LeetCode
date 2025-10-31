class Solution(object):
    def isAnagram(self, s, t):
        freq = [0] * 26

        for i in s:
            idx = ord(i) - ord("a")
            freq[idx] += 1

        for j in t:
            idx = ord(j) - ord("a")
            freq[idx] -= 1

        if freq == [0]*26:
            return True

        return False