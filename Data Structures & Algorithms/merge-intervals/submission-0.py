class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                currInterval = res[-1]
                if interval[0] > currInterval[1]:
                    res.append(interval)
                else:
                    currInterval[0] = min(currInterval[0], interval[0])
                    currInterval[1] = max(currInterval[1], interval[1])
                    res[-1] = currInterval

        return res