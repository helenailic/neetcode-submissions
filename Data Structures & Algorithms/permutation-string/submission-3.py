from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal_char_freqs = defaultdict(int)
        for c in s1:
            goal_char_freqs[c] += 1

        char_freqs = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            char_freqs[s2[r]] += 1

            while (r-l+1) > len(s1):
                char_freqs[s2[l]] -= 1
                if char_freqs[s2[l]] == 0:
                    del char_freqs[s2[l]]
                l += 1

            if char_freqs == goal_char_freqs:
                return True

        return False
                
