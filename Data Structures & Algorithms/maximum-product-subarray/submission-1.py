class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp[i] is minProduct/maxProduct of subarray ending at i
        dp_min = [float("inf")] * len(nums)
        dp_max = [float("-inf")] * len(nums)
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]

        for i in range(1, len(nums)):
            dp_min[i] = min(nums[i], nums[i]*dp_min[i-1], nums[i]*dp_max[i-1])
            dp_max[i] = max(nums[i], nums[i]*dp_min[i-1], nums[i]*dp_max[i-1])

        return max(max(dp_min), max(dp_max))