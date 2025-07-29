class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 1000000
        max_profit = 0
        
        for i in range(len(prices)):
            
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                if profit > max_profit:
                    max_profit = profit

    

        return max_profit
            
