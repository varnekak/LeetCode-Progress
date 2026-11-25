class Solution(object):
    def maxProfit(self, prices):
        list =[]
        max = 0
        min = prices[0]
        n = len(prices)
        for i in range (n):
            if prices[i]<min:
                min = prices[i]
                 
            if prices[i]-min > max:
                max = prices[i] - min
        return max