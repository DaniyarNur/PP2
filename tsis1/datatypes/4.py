pi = 0
sign = 1
for i in range(1, 20, 2):
    pi = pi + (sign * 4 / i)
    sign *= -1
print(pi)
