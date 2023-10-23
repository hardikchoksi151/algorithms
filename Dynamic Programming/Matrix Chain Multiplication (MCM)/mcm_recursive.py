import sys

def solve(arr,l,r):
    # Bound Check
    if l >= r:
        return 0
    min = sys.maxsize
    for k in range(l,r):
        left_subarr = solve(arr, l, k)
        right_subarr = solve(arr, k, r)
        temp_ans = left_subarr + right_subarr + arr[l-1] * arr[k] * arr[r]
        if temp_ans < min:
            min = temp_ans
    return min

# driver code
arr = [1,2,3,4,3]
print(solve(arr, 1, len(arr)-1))