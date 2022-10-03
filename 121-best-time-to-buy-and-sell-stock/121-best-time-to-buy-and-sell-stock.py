class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        left= 0
        right= 1
        
        while(left<right and right!=len(prices)):
            if(prices[left]>prices[right]):
                left=right
                right=right+1
            else:
                profit= prices[right]-prices[left]
                max_profit=max(profit,max_profit)
                
                right=right+1
        return max_profit
        