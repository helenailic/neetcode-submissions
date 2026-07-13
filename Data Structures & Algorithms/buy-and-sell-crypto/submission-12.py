class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        currmin = prices[0]
        maxp = 0

        while (r < len(prices)):
            currmin = min(prices[l], currmin)
            maxp = max(maxp, prices[r]-currmin)

            l += 1
            r += 1

        return maxp