a = input().split() 
n = (len(a) - int(input())) % len(a)
print(*a[n::], end = ' ')
print(*a[:n:])