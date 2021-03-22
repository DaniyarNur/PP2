#from collections import Counter

from collections import Counter
from sys import stdin

a = stdin.read().split()

ans = Counter(a)

print(*sorted(ans, key=ans.get, reverse=True), sep='\n')