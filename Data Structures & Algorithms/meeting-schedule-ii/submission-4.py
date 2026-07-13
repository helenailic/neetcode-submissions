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
        #min days to schedule all meetings without conflicts
        #if overlapping, need diff day
        numDays = 1
        res = []
        intervals.sort(key=lambda x:x.start)
        ends = set()
        
        #number of overlapping intervals 
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
                ends.add(interval.end)
            else:
                weGood = False
                theEnd = -1
                for end in ends:
                    if interval.start >= end:
                        weGood = True
                        theEnd = end
                if theEnd != -1:
                    ends.remove(theEnd)
                if not weGood:
                    numDays += 1
                res.append(interval)
                ends.add(interval.end)

        return numDays
