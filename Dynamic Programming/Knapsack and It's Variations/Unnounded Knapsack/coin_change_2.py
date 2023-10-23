import sys
# Tech-dose explaination works


def coin_change_2(sum, coin, n):
    dp = [[-1 for i in range(sum + 1)] for i in range(n + 1)]

    # Choice diagram
    for i in range(n + 1):
        for j in range(sum + 1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = sys.maxsize
            elif coin[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coin[i - 1]], dp[i - 1][j])

    if dp[n][sum] == sys.maxsize:
        return -1

    return dp[n][sum]


coins = [9, 6, 5, 1]
sum = 11
n = len(coins)
print(coin_change_2(sum, coins, n))
