n = int(input("请输入n的值为="))
m = 2
while m < n:
    if n % m == 0:
        break
    m += 1
if m == n:
    print(f"{n}是一个质数")
else:
    print(f"{n}不是一个质数")
