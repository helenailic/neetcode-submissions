from collections import defaultdict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #connect speed and position arrays
        my_dict = {} #position:speed
        for i, car in enumerate(position):
            my_dict[car] = speed[i]
        
        #sort positions in ascending order 
        sorted_positions = sorted(position, reverse=True)
        stack = []

        #now generate sorted speeds array
        sorted_speeds = [0] * len(sorted_positions)
        for i, position in enumerate(sorted_positions):
            sorted_speeds[i] = my_dict[position]
        
        for i, car in enumerate(sorted_positions):
            hours = (target - sorted_positions[i]) / sorted_speeds[i] 

            if len(stack) == 0:
                stack.append(hours)
            else:
                if hours > stack[len(stack)-1]:
                    stack.append(hours)
                #otherwise do nothing cuz it's same fleet 
            
        return len(stack)

