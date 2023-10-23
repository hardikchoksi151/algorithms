def knapSack(w, wt, val, n, dp):
    # initial conditions
    if n == 0 or w == 0:
        return 0
    if dp[w][n] != -1:
        return dp[w][n]
    # If weight is higher than capacity then it is not included
    if (wt[n-1] > w):
        dp[n][w] = knapSack(w, wt, val, n-1, dp)
        return dp[w][n]
    # return either nth item being included or not
    else:
        dp[w][n] = max(val[n-1] + knapSack(w-wt[n-1], wt, val, n-1, dp),
                   knapSack(w, wt, val, n-1, dp))
        return dp[w][n]

# To test above function
val = [60, 100, 120]
wt = [10,20,30]
W = 50
n = len(val)
dp = [ [ -1 for i in range(n+1) ] for j in range(W+1) ]
print(knapSack(W, wt, val, n, dp))
