class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf') # any value is lower than this
        for price in prices:
            min_price = min(min_price, price) # the lowest price up to this day
            profit = price - min_price # the profit we can make selling at this day
            max_profit = max(max_profit, profit) # the most we could have made
        return max_profit
