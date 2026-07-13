
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0 
        chars = set()

        l = 0
        for r in range(len(s)):
            if s[r] in chars:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
                #now l at next stop after r
            else:
                chars.add(s[r])
                maxLength = max(maxLength, r-l+1)


        return maxLength