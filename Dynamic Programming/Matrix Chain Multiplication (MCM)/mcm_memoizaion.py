import sys
dp = [[-1 for i in range(100)] for i in range(100)]

def solve(arr, l, r):
    if l >= r:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]
    min = sys.maxsize
    for k in range(l, r):
        temp_ans = solve(arr, l, k) + solve(arr, k+1, r) + arr[l-1] * arr[k] * arr[r]
        if temp_ans < min:
            min = temp_ans
            dp[l][r] = min
    return dp[l][r]

# driver code
arr = [1,2,3,4,3]
print(solve(arr, 1, len(arr)-1))