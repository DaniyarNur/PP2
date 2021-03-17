def IsPointInSquare(x, y):
    if abs(y) <=  1 - abs(x):
        return True
    else:
        return False
x = float(input()) 
y = float(input()) 


if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
