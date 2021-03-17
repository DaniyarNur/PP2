def IsPointInSquare(x, y):
    if x ** 2 <= 1 and y ** 2 <= 1:
        return True
    else:
        return False
x = float(input()) 
y = float(input()) 
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")