class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            max_wealth = max(max_wealth, wealth)

        return max_wealth