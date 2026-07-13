class Solution:
    def rob(self, nums: List[int]) -> int:
        #CAN'T ROB BOTH HOUSES, SO LET'S TRY BOTH!
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[1], nums[0], nums[2])

        #exclude last 
        dp1 = [None] * (len(nums)-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])

        #exclude first 
        nums_minus_first = nums[1:]
        dp2 = [None] * (len(nums)-1)
        dp2[0] = nums_minus_first[0]
        dp2[1] = max(nums_minus_first[0], nums_minus_first[1])
        for i in range(2, len(nums_minus_first)):
            dp2[i] = max(dp2[i-1], nums_minus_first[i] + dp2[i-2])

        return max(dp1[-1], dp2[-1])