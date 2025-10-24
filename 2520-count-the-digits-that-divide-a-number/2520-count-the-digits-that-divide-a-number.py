class Solution(object):
    def countDigits(self, num):
        count = 0
        str_num = str(num)

        for i in str_num:
            if num % int(i) == 0:
                count += 1

        return count