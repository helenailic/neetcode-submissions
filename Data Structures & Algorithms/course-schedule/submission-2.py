class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #b before a
        #0 to numCourses-1 labels 
        #cycle detection
        def hasCycle(i, visited, visiting, prereq_dict):
            if i in visiting:
                return True
            if i in visited:
                return False
            visiting.add(i)
            if i in prereq_dict:
                for val in prereq_dict[i]:
                    if hasCycle(val, visited, visiting, prereq_dict):
                        return True
            visiting.remove(i)
            visited.add(i)

        visiting = set()
        visited = set()
        prereq_dict = {}
        for val in prerequisites:
            if val[1] in prereq_dict:
                prereq_dict[val[1]].append(val[0])
            else:
                prereq_dict[val[1]] = []
                prereq_dict[val[1]].append(val[0])

        for i in range(numCourses):
            if hasCycle(i, visited, visiting, prereq_dict):
                return False

        return True