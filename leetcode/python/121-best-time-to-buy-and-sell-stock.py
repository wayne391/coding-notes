class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        min_price, max_profit = float('inf'), 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(max_profit, p-min_price)
        return max_profit