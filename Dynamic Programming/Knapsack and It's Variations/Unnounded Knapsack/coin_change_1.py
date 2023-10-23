# I/P: Given Coin Array & Sum
# O/P: number of ways you can match sum or count of subsets of coin set whose sum is equal to given sum.
# Similar to count of subset sum & unbounded knapsack
def coin_change_1(sum, coin, n):
    dp = [[False for i in range(sum + 1)] for j in range(n + 1)]
    # Initialization
    for i in range(sum+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 1
    # choice diagram
    for i in range(n+1):
        for j in range(sum+1):
            if coin[i-1] > sum:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin[i-1]]

    return dp[n][sum]


# Driver Code
coin = [1, 2, 3]
print(coin_change_1(3, coin, len(coin)))
