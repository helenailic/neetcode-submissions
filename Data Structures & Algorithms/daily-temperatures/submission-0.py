class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures 
        stack = []
        result = [0] * len(temps)
        for i, temp in enumerate(temps):
            if len(stack) != 0 and temp > stack[len(stack)-1]:
                while len(stack) != 0 and temp > stack[len(stack)-1]:
                    result[temps.index(stack[len(stack)-1])] = i - temps.index(stack[len(stack)-1])
                    temps[temps.index(stack[len(stack)-1])] = 'x' #tombstone value
                    stack.pop()
                stack.append(temp)
            else:
                stack.append(temp)


        return result