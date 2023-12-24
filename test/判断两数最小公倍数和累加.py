i = 0
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(sum)

i = 0
b = 0
while i <= 100:
    b = b + i
    i += 2
print(b)


a = eval(input("请输入一个1,到9的整数"))
n = eval(input("请输入累加的最大位数"))
c = 0
i = 0
addend = 0
while i <= n:
    i += 1
    addend = addend * 10 + a
    c = c + addend
print(c)


a = eval(input("请输入一个整数"))
b = eval(input("请再输入一个整数"))
if a > b:
    maxnumber = a
elif a < b:
    maxnumber = b
else:
    print()
g = maxnumber
while g <= a * b + 1:
    if g % a == 0 and g % b == 0:
        print(f"俩个数最小公倍数为{g}")
        break
    g += 1

A = eval(input("请输入一个整数"))
B = eval(input("请再输入一个整数"))
if a > b:
    minnumber = b
elif a < b:
    minnumber = a
else:
    print()
g = minnumber
while g == 0:
    if g % A == 0 and g % B == 0:
        print(f"俩个数最大公约数为{g}")
        break
    g -= 1


money = 10
beers = money//2
caps = 0
bottles = 0
count = 0
if beers > 0:
    for i in range(1, beers):
        caps = caps + beers
        bottles = bottles + beers
        count = count + beers
        beers = 0
        if caps >= 4:
            beers = beers + caps // 4
            caps = caps % 4
            if bottles >= 2:
                beers = beers + bottles // 2
                bottles = bottles % 2
            if beers == 0 and caps < 4 and bottles < 2:
                break
print(beers)
print(caps)
print(bottles)