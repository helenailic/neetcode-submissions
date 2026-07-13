from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        associated_speeds = defaultdict(int) #pos: speed
        for i, p in enumerate(position):
            associated_speeds[p] = speed[i]
        
        sorted_positions = sorted(position, reverse=True)
        sorted_speeds = []
        for p in sorted_positions:
            sorted_speeds.append(associated_speeds[p])

        my_stack = []
        for i, p in enumerate(sorted_positions):
            hours = (target-sorted_positions[i])/sorted_speeds[i]
            if len(my_stack) == 0:
                my_stack.append(hours)
            else:
                if hours > my_stack[-1]:
                    my_stack.append(hours)

        return len(my_stack)

        
