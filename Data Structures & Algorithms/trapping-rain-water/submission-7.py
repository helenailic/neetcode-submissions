
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
            else:
                if height[i] > prefix[i-1]:
                    prefix[i] = height[i]
                else:
                    prefix[i] = prefix[i-1]

        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffix[i] = height[i]
            else:
                if height[i] > suffix[i+1]:
                    suffix[i] = height[i]
                else:
                    suffix[i] = suffix[i+1]

        max_area = 0
        for i, bar in enumerate(height):
            max_area += max(0,min(prefix[i], suffix[i])-height[i])

        return max_area

