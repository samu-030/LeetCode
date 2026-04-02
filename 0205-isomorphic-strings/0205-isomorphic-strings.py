class Solution(object):
    def isIsomorphic(self, s, t):
        return [s.index(c) for c in s] == [t.index(c) for c in t]