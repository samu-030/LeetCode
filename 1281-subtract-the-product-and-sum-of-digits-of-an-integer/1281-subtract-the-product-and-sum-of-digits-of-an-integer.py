class Solution(object):
    def subtractProductAndSum(self, n):
        pdt,sum_o_d = 1, 0
        n1 = str(n)
        for i in n1:
            pdt *= int(i)
            sum_o_d += int(i)

            diff = pdt - sum_o_d

        return diff

        