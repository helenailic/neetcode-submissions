class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy and sell multiple times 
        #if you sell, no buying another on next day 
        #1 neetcoin at a time
        #return max profit 
        #dp[i][j] max profit, holding stock
        #dp[i][0] max profit on that day if you dont hold stock on that day 
        #dp[i][1] max profiton that day if you do hold stock on that day 
        dp = []
        for i in range(len(prices)):
            row = []
            row.append(0)
            row.append(0)
            dp.append(row)
        dp[0][0] = 0           # Day 0, no stock
        dp[0][1] = -prices[0]

        #dp start from loop i = 1
        for i in range(1, len(prices)):
            for j in range(2):
                #if j == 0 (not holding stock on this day)
                if j == 0:
                    #doing nothing today: dp[i-1][j]
                    #selling today: dp[i-1][1] + prices[i]
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                #if j == 1 (holding stock on this day)
                if j == 1:
                    #doing nothing today: dp[i-1][j]
                    #buying today: dp[i-1][0] + prices[i]
                    dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[len(prices)-1][0]






