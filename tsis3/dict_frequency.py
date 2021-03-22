from sys import stdin

freq = dict()

a = stdin.read().split()    #splitlines() creates a list of lines, not single words

for x in a:
    freq[x] = freq.setdefault(x, 0) - 1

print(*[x[1] for x in sorted(list(zip(freq.values(), freq.keys())))], sep = "\n")


        
