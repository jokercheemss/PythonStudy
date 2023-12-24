while True:
    n = int(input("请输入一个大于6的1偶数"))
    if n > 5 and n % 2 == 0:
        break
maxp = n // 2
for p in range(2, maxp+1, 2):
    flag = True
# 判断p是否为素数
    for i in range(2, p):
        if p % i == 0:
            flag = False
            break
    if flag:
        q = n-p
        for i in range(2, q):
            if q % i == 0:
                flag = False
                break
    if flag:
        print(n, "=", p, "+", q)
