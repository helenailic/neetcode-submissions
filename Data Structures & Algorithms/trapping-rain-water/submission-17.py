class Solution:
    def trap(self, height: List[int]) -> int:
        #fills up to min between the two
        #left hand side, the right is constrained by not having taller before then
        res = 0
        left_max = 0
        right_max = 0
        l,r = 0, len(height)-1
        #keep track of left max and right max
        while l < r:
            #2, 1
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                curr_water = max(0, left_max-height[l])
                res += curr_water
                l += 1
            else:
                curr_water = max(0, right_max-height[r])
                res += curr_water
                r -= 1

        return res