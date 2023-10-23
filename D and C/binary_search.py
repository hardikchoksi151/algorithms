# Recursive function for binary Search
def binary_search_recursive(arr, x, start, end):

    if start <= end:

        mid = (start + end) // 2
        # Choice diagram
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search_recursive(arr, x, start, mid-1)
        else:
            return binary_search_recursive(arr, x, mid+1, end)

# Iterative function for bs
def binary_search_iterative(arr, x):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

# Driver code
arr = [1,2,3,4,5,6,7,8,9]
print('Recursive:',binary_search_recursive(arr, 5, 0, len(arr) - 1))
print('Iterative:',binary_search_iterative(arr, 5))
