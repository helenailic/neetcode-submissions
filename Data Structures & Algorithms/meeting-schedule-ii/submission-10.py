import heapq
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
        sorted_intervals = intervals.sort(key=lambda x:x.start)
        maxCount = 0
        count = 0
        heap = []

        for interval in intervals:
            if len(heap) == 0 or interval.start < heap[0]:
                count += 1
                maxCount = max(maxCount, count)
                heapq.heappush(heap, interval.end)
            else:
                while len(heap) != 0 and interval.start >= heap[0]:
                    count -= 1
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
                count += 1
                maxCount = max(maxCount, count)

        return maxCount