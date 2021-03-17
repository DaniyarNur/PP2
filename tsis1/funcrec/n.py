def comb(n, k):
    if k == 1:
        return n
    if n == k or k == 0:
        return 1
    return(comb(n - 1, k) + comb(n - 1, k - 1))


n = int(input())
k = int(input())
print(comb(n, k))