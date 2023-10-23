def counting_sort(a, b, k):
    c = [0 for i in range(k+1)]  # creating middle array c
    # store the count of each element of a
    for i in a:
        c[i] += 1
    # take prefix sum of c
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    # right shift array c by one unit [c = c>>1]
    c = [0] + c[:-1]
    # scan a from left to right and add elements in output array
    for i in a:
        b[c[i]] = i
        c[i] += 1

# driver code
a = [3, 6, 4, 1, 3, 4, 1, 4, 2]
b = [0 for i in range(len(a))]  # output array
counting_sort(a, b, max(a))
print(b)