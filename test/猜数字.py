number = int(input("请输入你第一次猜想的数字"))
if number == 10:
    print("这位才是重量级")

    number = int(input("猜错了"))
elif number == 10:
    print("猜对了")
    number = int(input("错了"))
elif number == 10:
    print("猜对了")
    print("最后一次机会也没了哦")
else:
    print("你就是个几把")


