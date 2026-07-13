"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        backlog = []
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if len(backlog) == 0:
                backlog.append(interval)
            else:
                currInterval = backlog[-1]
                if interval.start < currInterval.end:
                    return False
                else:
                    backlog.append(interval)

        return True