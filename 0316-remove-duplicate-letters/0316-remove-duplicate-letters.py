from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):

        count = Counter(s)
        seen = set()
        res = []

        for ch in s:

            count[ch] -= 1

            if ch in seen:
                continue

            while (res and ch < res[-1] and count[res[-1]] > 0):
                seen.remove(res.pop())

            seen.add(ch)
            res.append(ch)

        return "".join(res)