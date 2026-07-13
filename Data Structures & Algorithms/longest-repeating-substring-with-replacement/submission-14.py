class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        char_freqs = defaultdict(int)
        longestString = 0
        l = 0
        for r in range(len(s)):
            #add it to the set
            char_freqs[s[r]] += 1
            maxFreq = max(maxFreq, char_freqs[s[r]])

            #while loop for conditon validity 
            #numReplacements = 
            while (r-l+1) - maxFreq > k:
                char_freqs[s[l]] -= 1
                if char_freqs[s[l]] == 0:
                    del char_freqs[s[l]]
                l += 1

            #update return value
            longestString = max(longestString, r-l+1)

        return longestString