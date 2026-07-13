from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #number of times you need to call bfs 
        #edges[i] -- edge between a and b
        #n nodes 
        #go through all nodes 
        def bfs(i, edges_dict, visited):
            queue = deque()
            visited.add(i)
            queue.append(i)
            while len(queue) != 0:
                curr = queue.popleft()
                #go through neighbors
                if curr in edges_dict:
                    for val in edges_dict[curr]:
                        if val not in visited:
                            visited.add(val)
                            queue.append(val)
                

        edges_dict = {} #node: the things it's connected to (both ways!
        for edge in edges:
            if edge[0] in edges_dict:
                edges_dict[edge[0]].append(edge[1])
            else:
                edges_dict[edge[0]] = []
                edges_dict[edge[0]].append(edge[1])

            if edge[1] in edges_dict:
                edges_dict[edge[1]].append(edge[0])
            else:
                edges_dict[edge[1]] = []
                edges_dict[edge[1]].append(edge[0])

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i, edges_dict, visited)

        return count
