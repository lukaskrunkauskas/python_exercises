#Raskite didžiausią bendrą dviejų skaičių daliklį.
n = int(input())
for i in range(0, n):
    inp = input()
    xy = inp.split(" ")
    x, y = (int(xy[0]), int(xy[1]))
    while x and y:
        if x > y:
            x %= int(y)
        else:
            y %= int(x)
    dbd = x + y
    print(dbd)
