class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # Case 1: current interval ends before new one starts → add it
            if interval[1] < newInterval[0]:
                res.append(interval)
            # Case 2: current interval starts after new one ends → add new one, then update
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval  # hand off
            # Case 3: overlap → merge
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res
