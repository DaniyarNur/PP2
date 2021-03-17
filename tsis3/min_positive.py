min = 1000
for x in [int(x) for x in input().split()]:
    if 0 < x and x < min:
        min = x
print(min)
