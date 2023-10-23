def sub_set_sum_count(sum, arr, n):
	dp = [[False for i in range(sum + 1)] for j in range(n + 1)]
	# Initialization
	for i in range(sum+1):
		dp[0][i] = 0
	for i in range(n+1):
		dp[i][0] = 1

	for i in range(n + 1):
		for j in range(sum + 1):
			# Choice Diagram
			if arr[i-1] > j: # exclude
				dp[i][j] = dp[i - 1][j]
			else: # include or exclude
				dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]

	return dp[n][sum] 
# Driver Code
arr = [2,3,5,6,8,10]
print(sub_set_sum_count(10, arr, len(arr)))