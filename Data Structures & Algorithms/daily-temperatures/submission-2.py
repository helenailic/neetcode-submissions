class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            stack.append(temperatures[i])

        for i in range(len(temperatures)):
            stack.pop(0)
            days = 0
            for num in stack:
                days += 1
                if num > temperatures[i]:
                    result[i] = days
                    break

        return result 
        