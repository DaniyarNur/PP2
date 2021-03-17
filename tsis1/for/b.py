a = int(input())
b = int(input())
c = ''
if (a > b):
    for i in range(a, b -1, -1):
        c += str(i) + ' '
for i in range(a, b +1):
    c += str(i) + ' '
print(c)