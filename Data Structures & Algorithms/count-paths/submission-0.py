class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #num possible unique paths from [0][0] to [m-1][n-1]
        #each spot should store NUMBER of ways to get there 
        #can only move DOWN or RIGHT so can get there from TOP or LEFT 
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue 
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
