from collections import defaultdict 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1counts = defaultdict(int) #char: frequency
        for c in s1:
            s1counts[c] += 1

        l = 0
        s2counts = defaultdict(int)
        for r in range(len(s2)):
            #expand window
            s2counts[s2[r]] += 1

            #while invalid: shrink window from left - condition is to maintain window of length l1
            if (r-l+1 > len(s1)):
                s2counts[s2[l]] -= 1
                if s2counts[s2[l]] == 0:
                    del s2counts[s2[l]]
                l += 1

            #update result
            if s2counts == s1counts:
                return True
            

        return False