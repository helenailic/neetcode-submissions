class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        currMax = 0
        s = []
        heights.append(0)

        for i, h in enumerate(heights):
            while len(s) > 0 and h < s[-1][0]:
                val = s.pop(-1)
                candMax = 0
                if len(s) == 0:
                    candMax = val[0] * i
                else:
                    candMax = val[0] * (i-s[-1][1]-1)
                currMax = max(currMax, candMax)

            s.append((h,i))

        return currMax