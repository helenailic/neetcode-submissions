class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        curr_min = prices[0]
        curr_buying_idx = 0
        curr_selling_idx = 1
        max_profit = 0
        while curr_selling_idx < len(prices):
            if prices[curr_buying_idx] < curr_min:
                curr_min = prices[curr_buying_idx]

            curr_profit = prices[curr_selling_idx] - curr_min
            if curr_profit > max_profit:
                max_profit = curr_profit 
            
            curr_buying_idx += 1
            curr_selling_idx += 1

        return max_profit

