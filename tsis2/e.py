n = input()
l = [int(n[i:i+1]) for i in range(len(n))]

sum = 0
product = 1
for i in l:

    sum += i
    product *= i
print(product - sum)