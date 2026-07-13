"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        maxCount = 0
        count = 0
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        s = 0
        e = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                maxCount = max(maxCount, count)
                s += 1
            else:
                count -= 1
                e += 1

        return maxCount