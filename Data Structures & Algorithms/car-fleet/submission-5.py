class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        associated_speeds = {} #position: speed
        for i in range(len(position)):
            associated_speeds[position[i]] = speed[i]

        position.sort()

        #GO IN REVERSE
        for i in range(len(position)-1, -1, -1):
            time = (target-position[i])/associated_speeds[position[i]]
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)