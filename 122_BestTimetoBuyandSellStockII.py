class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bought = 0
        maxProfit = 0
        
        for i in range(len(prices)):

            if i < len(prices)-1 and prices[i] < prices[i+1]:
                maxProfit += (prices[i+1]-prices[i])


        return maxProfit

        
