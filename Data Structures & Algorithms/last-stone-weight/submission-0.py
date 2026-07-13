import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #each step choose 2 heaviest stones and smash together 
        #make max heap, adding remaining to the heap 
        q = []
        for stone in stones:
            heapq.heappush(q, -1 * stone)
        
        while len(q) > 1:
            first = -1 * heapq.heappop(q)
            second = -1 * heapq.heappop(q)
            if first < second:
                second = second - first
                heapq.heappush(q, -1 * second)
            if second < first:
                first = first - second
                heapq.heappush(q, -1 * first)

        if len(q) == 0:
            return 0
        else:
            return -1 * q[0]
