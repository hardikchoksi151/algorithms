def naive_matching(S, P):
    n = len(S)
    m = len(P) # window size
    for i in range(n - m + 1):
        j = 0
        while (j < m):
            if (S[i + j] != P[j]):
                break
            j += 1

        if (j == m):
            print(f'pattern found at index: {i}')
    
# Driver code
if __name__ == '__main__':
    S = 'AABAACAADAABAAABAA'
    P = 'AABA'
    naive_matching(S, P)