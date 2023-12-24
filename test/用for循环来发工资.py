import random


def a(x):
    if x <= 36.5:
        print("体温正常")
    else:
        print("体温过高")

a(40)

money = 10000
for i in range(1, 20):
    number = random.randint(1, 5)
    if number < 5:
        print(f"员工{i}绩效分{number},无法领取工资")
        continue
    elif number >= 5:
        money = money - 1000
        print(f"员工{i}领取工资,绩效分{number},领取工资1000元,还剩{money}元")
    elif money == 0:
         break
    print("工资发完了,下次再来")
