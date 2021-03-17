def summ():
    a = int(input())
    if (a == 0):
        print(a)
        return a
    if summ() == 0:
        print(a)
        return 0
summ()