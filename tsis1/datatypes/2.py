def factorial(x):
    s = 1
    if x == 0:
        return s
    for i in range(1, x + 1):
        s = s * i
    return s

print(factorial(20))