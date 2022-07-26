
class Solution:
    # Basic Approach
    # def maxProfit(self, prices: List[int]) -> int:
    #     days = len(prices)
    #     profit = 0
    #     for i in range(days):
    #         for j in range(i+1,days):
    #             profit = max((j-i),profit)
    #     return profit
    # Optimised
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        price = float('inf')
        profit = 0
        for i in range(days):
            price = min(price,prices[i])
            profit = max(profit,prices[i]-price)
        return profit