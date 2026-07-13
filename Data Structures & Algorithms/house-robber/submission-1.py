class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        #amount of money the ith house has 
        #can't rob 2 adjacent houses (i, i+1) or (i, i-1)
        #return max amount of money you can rob without alerting the police 
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        #max money you can rob from first i+1 houses without tripping alarm
        #not MINIMIZING cost, but MAXIMIZING loot
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        #rob this house, then can't rob i-1. 
        #skip this house, then take max you had up to i-1
        return dp[len(nums)-1]
            