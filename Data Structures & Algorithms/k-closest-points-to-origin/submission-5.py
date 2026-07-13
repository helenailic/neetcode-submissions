import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #2d array points, int k
        #points[i] = [xi, yi]
        #k closest points to origin 

        #because i use heap for ordering, need to do it based on distance!
        #heapq always uses first element in tuple to keep order 

        heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) < k:
                heapq.heappush(heap, (-1*dist, point))
            else: 
                if dist < -1*heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-1*dist, point))

        top_k = []
        for t in heap:
            top_k.append(t[1])
        return top_k
