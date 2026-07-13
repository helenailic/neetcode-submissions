class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #unlimited: so move forward in dp
        #make length of dp amount + 1
        #each spot is the min num of coins to get to that amount
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]