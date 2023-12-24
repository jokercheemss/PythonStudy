def funa(x, y=3, z=10):
    print("funa", x, y, z)


def funb(a, x=2):
    global y
    funa(4)
    print("funb", a, x, y)


y = 20
funa(1, 2, 3)
funb(70, 80)

