class Solution(object):
    def smallestSubsequence(self, s):

        freq = [0] * 26
        seen = [False] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []

        for ch in s:
            idx = ord(ch) - ord('a')

            freq[idx] -= 1

            if seen[idx]:
                continue

            while (result and ch < result[-1] and freq[ord(result[-1])-ord('a')] > 0):

                removed = result.pop()
                seen[ord(removed) - ord('a')] = False

            result.append(ch)
            seen[idx] = True

        return "".join(result)
        