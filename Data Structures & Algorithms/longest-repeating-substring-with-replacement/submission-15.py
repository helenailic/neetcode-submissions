from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        maxCharCount = 0
        maxChar = ""
        l = 0
        maxLength = float("-inf")
        for r in range(len(s)):
            char_counts[s[r]] += 1
            if char_counts[s[r]] > maxCharCount:
                maxCharCount = char_counts[s[r]]
                maxChar = s[r]

            while (r-l+1)-maxCharCount > k:
                char_counts[s[l]] -= 1
                if char_counts[s[l]] == 0:
                    del char_counts[s[l]]
                l += 1

            maxLength = r-l+1

        return maxLength 
            