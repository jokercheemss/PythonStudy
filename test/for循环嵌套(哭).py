name = "number"
for x in name:
    print(x)
for x in range(1, 10, 2):
    print(x)

i = 1
for a in range(i, 11):
    print("今天要送j%d朵玫瑰花" % a)

day = 1
flower = 1
for a in range(day, 101):
    print(f"今天是送j玫瑰花的第{a}天")
    for b in range(flower, 11):
        print(f"今天是第{a}天,这是送j的第{b}玫瑰花")
    if a == 100:
        print("j,今天是送花的第100天,我喜欢你")





















