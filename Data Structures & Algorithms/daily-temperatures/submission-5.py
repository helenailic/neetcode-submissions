class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [None for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if len(s) == 0:
                s.append((temp, i))

            while len(s) != 0 and temp > s[-1][0]:
                val = s.pop(-1)
                res[val[1]] = i-val[1]

            s.append((temp,i))

        for c in s:
            res[c[1]] = 0

        return res