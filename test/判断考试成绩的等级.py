week = eval(input("请输入一个0~6的整数"))
if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wesdnesday")
elif week == 4:
    print("Tursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 0:
    print("Sunday")

m = eval(input("请输入你的成绩"))
if 90 < m < 100:
    print("你的成绩为A")
elif 80 < m < 90:
    print("你的成绩为B")
elif 70 < m < 80:
    print("你的成绩为C")
elif 60 < m < 70:
    print("你的成绩为D")
elif 0 < m < 59:
    print("你的成绩为E")
else:
    print("你输入的成绩不符合要求")


