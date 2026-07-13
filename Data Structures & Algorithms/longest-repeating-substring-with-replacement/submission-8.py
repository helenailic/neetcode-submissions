from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charFreqs = defaultdict(int)
        res = 0

        for r in range(len(s)):
            charFreqs[s[r]] += 1
            #check current window is valid
            while (r-l+1) - max(charFreqs.values()) > k:
                charFreqs[s[l]] -= 1
                l += 1

            #update result
            res = max(res, r-l+1)

        return res 