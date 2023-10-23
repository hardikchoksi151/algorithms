def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        i = 0
        j = gap
        while j < n:
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
            i += gap
            j = i + gap
            
        print(f"value of i and j and gap:{i},{j},{gap}")
        gap //= 2

a = [21,38,29,17,4,25,11,32,9]
shell_sort(a)
print(a)