class Solution(object):
    def addBinary(self, a, b):
        a = list(a)
        b = list(b)
        res = []
        carry = 0

        while a or b or carry:
            bit1 = int(a.pop()) if a else 0
            bit2 = int(b.pop()) if b else 0

            total = bit1 + bit2 + carry
            carry = total // 2
            res.append(str(total % 2))

        return ''.join(res[::-1])