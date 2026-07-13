class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([temp, i])
            else:
                while len(stack) != 0 and temp > stack[len(stack)-1][0]:
                    result[stack[len(stack)-1][1]] = i - stack[len(stack)-1][1]
                    stack.pop()
                
                stack.append([temp, i])

        return result 
        