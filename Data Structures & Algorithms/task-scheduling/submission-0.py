import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #task[i] -- uppercase english char 
        #integer n
        #identical tasks must be separated by at least n cpu cycles 
        #return min num cpu cycles to complete all tasks 
        
        #each cpu cycle, choose 'smartest' task atp
        #always run most frequent remaining task 

        #max heap with tuples (freq, task)
        freqs = {}
        for task in tasks:
            if task in freqs: 
                freqs[task] += 1
            else:
                freqs[task] = 1

        heap = []
        for key, value in freqs.items():
            heapq.heappush(heap, (-1 * value, key))

        cycles = 0
        queue = deque() #waiting room (freq_remaining, task, time_when_good)
        while queue or heap:
            val = 0
            if queue and queue[0][2] <= cycles:
                val = queue[0]
                queue.popleft()
                heapq.heappush(heap, (val[0], val[1]))
            
            if not heap:
                cycles = queue[0][2]
            else:
                val = heapq.heappop(heap)
                cycles += 1 
                val = (val[0]+1, val[1])
                if val[0] < 0:
                    queue.append((val[0], val[1], cycles+n))

        return cycles
