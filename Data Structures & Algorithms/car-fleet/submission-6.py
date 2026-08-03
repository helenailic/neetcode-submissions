class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_dict = {} #pos: speed 
        for i in range(len(position)):
            if position[i] not in my_dict:
                my_dict[position[i]] = []
            my_dict[position[i]].append(speed[i])

        sorted_positions = sorted(position)
        s = []
        for i in range(len(sorted_positions)-1, -1, -1):
            currPos = sorted_positions[i]
            time = (target-currPos)/my_dict[currPos][0]
            if len(s) == 0:
                s.append((currPos, time))
            else:
                if time > s[-1][1]:
                    s.append((currPos, time))
        
        return len(s)
