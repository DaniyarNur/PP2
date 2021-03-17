x = int(input())
print('YES') if (x % 4 == 0 and x % 100 != 0) or x % 400  == 0 else print('NO')