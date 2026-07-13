"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        maxCount = 0
        count = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                maxCount = max(maxCount, count)
                s += 1
            else:
                count -= 1
                e += 1

        return maxCount

