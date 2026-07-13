class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        front = 0
        back = len(heights)-1

        for height in heights:
            curr_area = (back-front) * min(heights[back], heights[front])
            if curr_area > max_area:
                max_area = curr_area;
            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1

        return max_area