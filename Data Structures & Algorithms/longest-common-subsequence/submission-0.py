class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #return length of longest common subsequence b/w 2 strings
        #2 state variables 
        #dp[i][j] -- store length of longest common subsequence of s1[:i] and s2[:j]

        dp = []
        for i in range(len(text1)+1):
            row = []
            for j in range(len(text2)+1):
                row.append(0)
            dp.append(row)

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]