class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(prefix[i-1], height[i])

        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(suffix[i+1], height[i])

        for i in range(len(height)):
            area += min(prefix[i], suffix[i])-height[i]


        return area