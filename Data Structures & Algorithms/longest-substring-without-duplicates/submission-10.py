class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        res = 0

        for r in range(len(s)):
            #check validity of window
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            #expand 
            chars.add(s[r])

            #update res
            res = max(res, r-l+1)

        return res