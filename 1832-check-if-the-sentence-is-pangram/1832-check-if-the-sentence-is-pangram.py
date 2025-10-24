class Solution(object):
    def checkIfPangram(self, sentence):
        freq = [0] * 26

        for ch in sentence:
            index = ord(ch) - ord('a')
            freq[index] = 1

        return sum(freq) == 26