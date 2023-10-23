def merge(left, right, arr):

    nL = len(left)
    nR = len(right)

    # i for left, j for right, k for arr
    i = j = k = 0

    while i < nL and j < nR :
        # check if first ele of left is less than or equal to first element of right
        if left[i] <= right[j]:
            # if it is, copy that ele to first ele of arr
            arr[k] = left[i]
            # bcoz first ele of left is used, increase i
            i += 1 
        # else (left_ele > right_ele)
        else:
            # copy first ele of right to first ele of arr
            arr[k] = right[j]
            # bcoz first ele of right is used, increase j
            j += 1
        # now, after making these choices, first position of arr is used, increase k
        k += 1
    
    '''
        now, there might be some elements still left in right or left sub-array,
        so, copy them directly to arr
    '''
    while i < nL:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < nR:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, n):
    # base condition
    if n == 1: return
    # choice diagram
    mid = n // 2
    # create two sub-arrays
    left = [0 for i in range(mid)]
    right = [0 for i in range(n - mid)]
    # fill these two sub-arrays
    for i in range(0, mid):
        left[i] = arr[i]
    for i in range(n - mid, n):
        right[i - mid] = arr[i]
    # sort these sub-arrays recursively
    merge_sort(left, len(left))
    merge_sort(right, len(right))
    # now, merge these sub-arrays in ascending order
    merge(left, right, arr)

# Driver Code
arr = [724, 521, 2, 98, 529, 31, 189, 451]
merge_sort(arr, len(arr))
print(arr)