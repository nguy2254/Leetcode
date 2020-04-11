class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i,price in enumerate(prices[0:len(prices)-1]):
            if prices[i+1]> prices[i]: maxProfit += (prices[i+1]-prices[i])
        return maxProfit
