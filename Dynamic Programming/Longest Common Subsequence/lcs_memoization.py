# I/P: Two strings X,Y
# O/P: length of lcs
# example: X = "abcdefgh", Y = "abzxdioh"
# output: ("abh") 3
def lcs(x, y, m, n, dp):
    # Base condition
    if n == 0 or m == 0:
        return 0
    # Check if value is stored in matrix
    if dp[m][n] != -1:
        return dp[m][n]
    # Choice diagram
    if x[m-1] == y[n-1]:
        dp[m][n] = 1 + lcs(x, y, m-1, n-1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(x, y, m-1, n, dp), lcs(x, y, m, n-1, dp))
        return dp[m][n]

# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
dp = [[-1 for j in range(n+1)] for i in range(m+1)]
print(lcs(X, Y, m, n, dp))
