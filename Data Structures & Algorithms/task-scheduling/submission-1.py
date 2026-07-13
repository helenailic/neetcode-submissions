import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #tasks[i] is char from a to z
        #same char tasks must be sep by n cpu cycles 
        #return min num of cpu cycles to complete all tasks

        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        time = 0
        #max heap of (num, task-char)
        heap = [] 
        for task, num in freq.items():
            heapq.heappush(heap, (-1 * num, task))

        #minHeap of: (time it's back in commission, task, freq)
        waitingRoom = []
        while heap or waitingRoom:
            while waitingRoom and time >= waitingRoom[0][0]:
                item = heapq.heappop(waitingRoom)
                heapq.heappush(heap, (-1*item[2], item[1]))

            if heap:
                item = heapq.heappop(heap)
                freq = -1*item[0]
                task = item[1]
                
                if (freq-1) != 0:
                    heapq.heappush(waitingRoom, (time+n+1, task, freq-1))

            time += 1


        return time
        
