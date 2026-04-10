class Solution(object):
    def maxProfit(self, prices):

        n = len(prices)

        min_price = prices[0]
        res = 0

        for i in range(1, n):
            min_price = min(min_price, prices[i])

            res = max(res, (prices[i] - min_price))

        return res