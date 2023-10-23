# I/P: Two strings X,Y
# O/P: length of lcs
# example: X = "abcdefgh", Y = "abzxdioh"
# output: ("abh") 3
def lcs(x, y, m, n):
    # Base condition
    if n == 0 or m == 0:
        return 0
    # Choice diagram
    if x[m-1] == y[n-1]:
        return 1 + lcs(x, y, m-1, n-1)
    else:
        return max(lcs(x, y, m-1, n), lcs(x, y, m, n-1))


# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y, len(X), len(Y)))
