def lcs(x, y, m, n):
    dp = [[-1 for j in range(n+1)] for i in range(m+1)]

    # Initialization
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    # Choice diagram
    for i in range(m+1):
        for j in range(n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i-1][j], dp[i][j-1])
    # for i in range(m+1):
    #     for j in range(n+1):
    #         print(dp[i][j], end=" ")
    #     print('') 
    return dp[m][n]
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
print(lcs(X, Y, m, n))
