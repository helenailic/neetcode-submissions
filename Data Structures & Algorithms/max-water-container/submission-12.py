class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = float("-inf")
        l, r = 0, len(heights)-1
        while l < r:
            maxWater = max(maxWater, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1

        return maxWater