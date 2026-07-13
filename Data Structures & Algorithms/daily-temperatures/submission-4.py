class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #temp, index

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append([temp,i])

        return result