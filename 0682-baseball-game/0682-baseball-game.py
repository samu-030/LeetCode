class Solution(object):
    def calPoints(self, operations):
        rcd = []
        for i in operations:
            if i == "C":
                rcd.pop()
            elif i == "D":
                rcd.append(2 * rcd[-1])
            elif i == "+":
                rcd.append(rcd[-1] + rcd[-2])
            else:
                rcd.append(int(i))

        return sum(rcd)

        