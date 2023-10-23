# given: i) set of non-negative intgrs
#		ii) sum value.
# find: if there exists a subset in our given set, such that
# 		sum of elements of subset = sum value
# if posssible return True else false
def sub_set_sum(sum, arr, n):
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

	# for i in range(n+1):
	# 	for j in range(sum+1):
	# 		print(dp[i][j], end=" ")
	# 	print("")
	return dp[n][sum] 

# To test above function
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
print(sub_set_sum(sum, set, n))