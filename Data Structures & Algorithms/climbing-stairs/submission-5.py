#index is a state, value is the solution for that state 
#are you able to climb a staircase from this state (0 or 1)
#each space is number of ways to get to top from that space 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n+1)

        def climb(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if memo[i] is not None:
                return memo[i]

            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]

        return climb(0)
        