a = eval(input("请输入a的值为:"))
b = eval(input("请输入b的值为:"))
c = eval(input("请输入c的值为:"))
if a != 0:
    key = b * b - 4 * a * c
    if key >= 0:
        x1 = -b + key * 0.5 / 2 * a
        x2 = -b - key * 0.5 / 2 * a
        print(f"方程组的一个根为{x1}")
        print(f"方程组的另一个根为{x2}")
    elif key < 0:
        print("方程无实根")
else:
    print("a不可以为0,请再输一次a的值")
    b = eval(input("请输入b的值为:"))
    c = eval(input("请输入c的值为:"))
    a = eval(input("请输入a的值为:"))
    key = b * b - 4 * a * c
    if key >= 0:
        x1 = -b + key * 0.5 / 2 * a
        x2 = -b - key * 0.5 / 2 * a
        print(f"方程组的一个根为{x1}")
        print(f"方程组的另一个根为{x2}")
    elif key < 0:
        print("方程无实根")