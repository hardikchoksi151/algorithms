def unbounded_knapsack(W, wt, val, n):
    dp = [[-1 for i in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j])
                
    return dp[n][W]

# To test above function
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]
W = 8
n = len(val)
print(unbounded_knapsack(W, wt, val, n))
