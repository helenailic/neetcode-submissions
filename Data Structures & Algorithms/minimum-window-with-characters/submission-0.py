from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        resleft = 0
        resright = float("inf")
        l = 0

        tcounts = defaultdict(int)
        for c in t:
            tcounts[c] += 1

        scounts = defaultdict(int)
        for r in range(len(s)):
            scounts[s[r]] += 1

            while all(scounts[c] >= tcounts[c] for c in tcounts):
                if (r-l+1)<(resright-resleft+1):
                    resleft = l
                    resright = r
                
                if s[l] in scounts:
                    scounts[s[l]] -=1
                l += 1


        if resright == float("inf"):
            return ""
        return s[resleft:resright+1]
