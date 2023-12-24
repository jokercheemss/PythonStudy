a = int(input("请输入一个整数:"))
b = int(input("请再输入一个整数:"))
if a>b:
    print(f"其中较大值为{a}")
elif a<b:
    print(f"其中较大值为{b}")

else:
    print("两值相同")