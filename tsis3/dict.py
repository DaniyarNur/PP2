n = int(input())
a = list()
for i in range(n):
    a.append(tuple(input().split()))

syn = dict(a)

syn.update(list(zip(syn.values(), syn.keys())))

print(syn[input()])