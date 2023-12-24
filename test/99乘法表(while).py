# 99乘法表
a = 1
while a <= 9:
    # 外层循环表示行数
    b = 1
    while b <= a:
        # 内层控制算式的改变
        print(f"{a}*{b}={a * b}\t", end='')
        b += 1
    a += 1
    print()
