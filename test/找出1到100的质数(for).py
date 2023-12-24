# 找出1,100之间的质数
for n in range(1, 101):
    m = 2
    while m < n:
        if n % m == 0:
            break
        m += 1
    if m == n:
        print(f"{n}是一个质数")
    else:
        continue
