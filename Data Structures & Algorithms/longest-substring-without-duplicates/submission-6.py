from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        maxlen = 0
        curr_chars = defaultdict(int) #char: index it's at 
        curr_chars[s[l]] = l

        while r < len(s):
            if s[r] in curr_chars and curr_chars[s[r]] >= l:
                maxlen = max(r-l, maxlen)
                l = curr_chars[s[r]]+1
                curr_chars[s[r]] = r
            else:
                curr_chars[s[r]] = r
            
            r += 1

        maxlen = max(r-l, maxlen)
        
        return maxlen