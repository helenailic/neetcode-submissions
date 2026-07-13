from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_counts = defaultdict(int)
        for c in t:
            t_counts[c] += 1

        formed = 0
        l = 0
        s_counts = defaultdict(int)
        minLength = float("inf")
        l_idx = 0
        r_idx = 0
        for r in range(len(s)):
            s_counts[s[r]] += 1
            if s[r] in t_counts and s_counts[s[r]] == t_counts[s[r]]:
                formed += 1
            
            while formed == len(t_counts):
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    l_idx = l
                    r_idx = r

                s_counts[s[l]] -= 1
                if s[l] in t_counts and s_counts[s[l]] < t_counts[s[l]]:
                    formed -= 1
                if s_counts[s[l]] == 0:
                    del s_counts[s[l]]
                l += 1
            
        if minLength == float("inf"):
            return ""
        return s[l_idx:r_idx+1]
