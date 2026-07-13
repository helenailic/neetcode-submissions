class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights)-1

        while right > left:
            if min(heights[left],heights[right])*(right-left) > maxArea:
                maxArea = min(heights[left],heights[right])*(right-left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 

        return maxArea 