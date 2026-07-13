class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #(index2-index1)*min(height1, height2)
        front_index = 0
        back_index = len(heights)-1
        max_area = 0

        for i in range(len(heights)):
            curr_area = (back_index-front_index)*min(heights[back_index],heights[front_index])
            if curr_area > max_area:
                max_area = curr_area
            
            #move pointer with smaller height
            if heights[front_index] < heights[back_index]:
                front_index += 1
            else:
                back_index -= 1

        return max_area