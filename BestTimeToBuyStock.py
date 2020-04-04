class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        reverse_prices = prices[::-1]
        profit = 0 
        sell_price = 0
        for price in reverse_prices:
            if price > sell_price:
                sell_price = price 
            if price <= sell_price:
                profit_new = sell_price - price
                if profit_new > profit: 
                    profit = profit_new 
        return profit 
