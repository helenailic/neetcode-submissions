"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        if len(sorted_intervals) == 0:
            return True

        for i, interval in enumerate(sorted_intervals):
            if i == len(sorted_intervals)-1:
                return True 
            
            if interval.end > sorted_intervals[i+1].start:
                return False 