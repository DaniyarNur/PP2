n = int(input())
s= ''
for i in range(10 ** n - 1, 10 ** (n - 1) - 1, -2):
    s += str(i) + ' '
print(s)