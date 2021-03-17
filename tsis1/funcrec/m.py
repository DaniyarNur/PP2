def phib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return(phib(n - 2) + phib(n - 1))


n = int(input())

print(phib(n + 1))