class Solution:
    def trap(self, height: List[int]) -> int:
        #prefix max in array from left to right
        prefix = []
        curr_prefix_max = 0
        for i in range(len(height)):
            prefix.append(curr_prefix_max)
            if height[i] > curr_prefix_max:
                curr_prefix_max = height[i]

        #suffix max in array from right to left 
        suffix = []
        curr_suffix_max = 0
        for i in range(len(height)-1, -1, -1):
            suffix.append(curr_suffix_max)
            if height[i] > curr_suffix_max:
                curr_suffix_max = height[i]
        suffix.reverse()

        #iterate through array with index i and calc total water at each position with formula
        max_area = 0
        for i in range(len(height)):
            max_area += max(0,min(prefix[i], suffix[i]) - height[i])

        return max_area