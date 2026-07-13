class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_idx = 0
        end_idx = 0
        longest = 0

        for i, c in enumerate(s):
            # Odd length
            curr_length = 1
            expanded = 1
            while i-expanded >= 0 and i+expanded < len(s):
                if s[i-expanded] == s[i+expanded]:
                    curr_length += 2
                else:
                    break
                expanded += 1
            if curr_length > longest:
                longest = curr_length
                start_idx = i - expanded + 1
                end_idx = i + expanded - 1

            # Even length
            curr_length = 0
            expanded = 0
            while i-expanded >= 0 and i+expanded+1 < len(s):
                if s[i-expanded] == s[i+expanded+1]:
                    curr_length += 2
                else:
                    break
                expanded += 1
            if curr_length > longest:
                longest = curr_length
                start_idx = i - expanded + 1
                end_idx = i + expanded

        return s[start_idx:end_idx+1]
