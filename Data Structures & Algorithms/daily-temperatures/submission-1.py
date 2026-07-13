class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures 
        stack = []
        result = [0] * len(temps)
        for i, temp in enumerate(temps):
            if len(stack) != 0 and temp > stack[len(stack)-1][0]:
                while len(stack) != 0 and temp > stack[len(stack)-1][0]:
                    result[stack[len(stack)-1][1]] = i - stack[len(stack)-1][1]
                    stack.pop()
                stack.append((temp,i))
            else:
                stack.append((temp,i))


        return result