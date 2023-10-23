def heapify(arr, curr, size):
    largest = curr
    l = 2*curr + 1
    r = 2*curr + 2
    
    if l < size and arr[l] > arr[largest]:
        largest = l

    if r < size and arr[r] > arr[largest]:
        largest = r

    if largest != curr:
        arr[curr], arr[largest] = arr[largest], arr[curr]
        heapify(arr, largest, size)

def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2 - 1, -1, -1):
        heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,0,i)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)
'''n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),'''