class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers!!!!!

        buying_index = 0
        selling_index = 1
        max_profit = 0

        while selling_index < len(prices):
            if prices[buying_index] < prices[selling_index]:
                profit = prices[selling_index] - prices[buying_index]
                max_profit = max(max_profit, profit)
            else:
                buying_index = selling_index
            selling_index += 1
            
        return max_profit
        
