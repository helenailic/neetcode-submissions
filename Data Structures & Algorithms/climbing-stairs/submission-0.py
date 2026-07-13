class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n+1) #store results of recursive calls 
        #when recursion called with specific values, return stored value that's already computed
        def climb(i):
            if i == n:
                return 1 #you've found one possible way
            if i > n:
                return 0 #this is not a possible way
            if i in memo:
                return memo[i]
            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]

        return climb(0)