def equal_sum(arr):
	sum = 0
	n = len(arr)
	for i in range(n):
		sum += arr[i]

	if sum % 2 != 0:
		return False
	else:
		sum = sum // 2
		dp = [[False for i in range(sum + 1)] for j in range(n + 1)]

		# Initialization
		for i in range(sum+1):
			dp[0][i] = False
		for i in range(n+1):
			dp[i][0] = True

		for i in range(n + 1):
			for j in range(sum + 1):
				# Choice Diagram
				if arr[i-1] > j: # exclude
					dp[i][j] = dp[i - 1][j]
				else: # include or exclude
					dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

		return dp[n][sum]

# driver code
arr = [ 1, 3, 3, 2, 3, 2 ]
print(equal_sum(arr))
 