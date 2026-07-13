from collections import defaultdict 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1counts = defaultdict(int)
        for c in s1:
            s1counts[c] += 1

        l = 0
        s2counts = defaultdict(int)
        for r in range(len(s2)):
            s2counts[s2[r]] += 1

            #condition is if window length becomes > length s1
            if r-l+1 > len(s1):
                s2counts[s2[l]] -= 1
                if s2counts[s2[l]] == 0:
                    del s2counts[s2[l]]
                l += 1

            #check result
            if s1counts == s2counts:
                return True

        return False