class Solution(object):
    def addStrings(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)
        res = ""
        carry = 0

        while num1 or num2 or carry:
            a = ord(num1.pop()) - ord("0") if num1 else 0
            b = ord(num2.pop()) - ord("0") if num2 else 0

            total = a + b + carry
            carry = total // 10
            res = str(total % 10) + res

        return res