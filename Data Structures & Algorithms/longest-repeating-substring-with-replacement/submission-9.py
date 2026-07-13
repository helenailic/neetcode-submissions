from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charFreqs = defaultdict(int) #char: frequency 

        for r in range (len(s)):
            charFreqs[s[r]] += 1
            #check window validness
            while ((r-l+1)-max(charFreqs.values()) > k):
                charFreqs[s[l]] -= 1
                l += 1

            #update res
            res = max(res, r-l+1)

        return res
