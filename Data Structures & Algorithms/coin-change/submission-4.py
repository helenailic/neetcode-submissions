class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins with dif numbers 
        #amount (target) --> this is like partition equal subset sum
        #fewest num of coins to make target 
        #dp[False, # Coins]
        #dp = min # of coins to make sum j
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(0, len(coins)):
            for j in range(coins[i], amount+1):
                if dp[j] == -1:
                    if dp[j-coins[i]] != -1:
                        dp[j] = dp[j-coins[i]] + 1
                else:
                    dp[j] = min(dp[j], dp[j-coins[i]] + 1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]