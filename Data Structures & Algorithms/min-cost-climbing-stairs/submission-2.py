#index is the step, value is the min cost to reach top of staircase from that step

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [None] * (len(cost)+1)

        def climb(i):
            if i >= len(cost):
                return 0
            if memo[i] is not None:
                return memo[i]
            memo[i] = cost[i] + min(climb(i+1), climb(i+2))
            return memo[i]

        return min(climb(0), climb(1))