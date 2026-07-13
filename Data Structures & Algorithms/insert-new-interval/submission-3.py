class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        added = False

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                if not added:
                    res.append(newInterval)
                    added = True
                res.append(intervals[i])
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        if not added:
            res.append(newInterval)

        return res