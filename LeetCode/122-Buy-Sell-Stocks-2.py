class Solution:
    # BASIC
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        profit = 0
        for day in range(days-1):
            if(prices[day+1] - prices[day] > 0):
                profit += prices[day+1] - prices[day]
        return profit