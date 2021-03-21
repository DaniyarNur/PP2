x = set(int(x) for x in input().split())
y = set(int(x) for x in input().split())
print(*sorted(x.intersection(y)))

#print(*sorted(set(input().split()).intersection(set(input().split()))))