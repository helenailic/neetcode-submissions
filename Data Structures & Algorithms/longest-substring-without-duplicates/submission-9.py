class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        charSet = set()
        l = 0
        maxlen = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[r])
            maxlen = max(maxlen, r-l+1)

        return maxlen