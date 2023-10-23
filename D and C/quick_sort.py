''' 
Partition function will find pivot and move all lesser ele than pivot to the left side of pivot
returns partitionIndex
'''
def partition(arr, start, end):
    # Suppose last ele is the pivot
    pivot = arr[end]
    pIndex = start
    for i in range(start, end - 1):
        # if element is lesser than pivot than swap positions 
        # with pIndex, (shifting lesser ele's to left of pivot)
        if arr[i] <= pivot:
            temp = arr[pIndex]
            arr[pIndex] = arr[i]
            arr[i] = temp
            pIndex += 1
    # now bring actal pivot to it's location
    temp = arr[pIndex]
    arr[pIndex] = pivot
    arr[end] = temp
    return pIndex

def quick_sort(arr, start, end):
   if start < end:
        pIndex = partition(arr, start, end)
        quick_sort(arr, start, pIndex - 1)
        quick_sort(arr, pIndex + 1, end)

# Driver Code
arr = [724, 521, 2, 98, 529, 31, 189, 451]
quick_sort(arr, 0, len(arr) - 1)
print(arr)