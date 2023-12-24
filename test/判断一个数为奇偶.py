num = int(input("请输入一个整数"))
if num % 2 == 0:
    print("该数为偶数")
else:
    print("该数为奇数")

for i in range(1, 4):
    for j in range(1, 4):
        for x in range(1, 4):
            if i != j and j != x and i != x:
                print(i, j, x)
