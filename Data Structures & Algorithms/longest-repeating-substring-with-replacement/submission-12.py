from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Number of replacements needed = window_size - max_freq
        #if number of replacements needed > k, shrink the window
        l = 0
        char_counts = defaultdict(int)
        maxFreq = 0
        longestWindow = 0

        for r in range(len(s)):
            char_counts[s[r]] += 1
            maxFreq = max(maxFreq, max(char_counts.values()))
            numRepsNeeded = (r-l+1)-maxFreq

            while numRepsNeeded > k:
                char_counts[s[l]] -= 1
                l += 1
                numRepsNeeded -= 1
            
            longestWindow = max(longestWindow, r-l+1)

        return longestWindow