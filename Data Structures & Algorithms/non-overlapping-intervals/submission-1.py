class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        res = []
        removed = 0
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                currInterval = res[-1]
                if currInterval[1] > interval[0]:
                    removed += 1
                else:
                    res.append(interval)

        return removed