#设置一个随机整数,并判断键盘录入数字是否等于随机数
import random
number = random.randint(1,100)

flag = True
count = 0
while flag:
    count += 1
    number_ = int(input("请输入一个随机整数"))
    if number_ == number:
        print("对了")
        flag = False
    else:
        if number_ > number:
            print("大了")
        else:
             print("小了")


print(f"你总共猜测了{count}次")