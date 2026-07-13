import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        for num in nums:
            if len(self.q) < k:
                heapq.heappush(self.q, num)
            elif num > self.q[0]:
                heapq.heappop(self.q)
                heapq.heappush(self.q, num)
        self.k = k
        

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            heapq.heappush(self.q, val)
        elif len(self.q) >= self.k and val > self.q[0]:
            heapq.heappop(self.q)
            heapq.heappush(self.q, val)
        return self.q[0]
        
        
