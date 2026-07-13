import heapq
#min heap = smallest element always at top
#min heap of size k
#k largest elements seen thus far 

class KthLargest:
    #kth largest integer in stream of vals, including dupes
    #not sorted
    #O(mlogk) time

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
