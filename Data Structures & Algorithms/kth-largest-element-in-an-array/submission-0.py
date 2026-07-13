import heapq
#kth largest element 
#min heap, but only of length k
#so first one is the kth largest element

#k = 2
#nums = 2 3 1 5 4
#heap = 2 3

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return kth largest 
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)

            elif len(heap) >= k:
                if heap and heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]
        