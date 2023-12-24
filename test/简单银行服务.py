def find(a):
    x = 0
    y = 0
    if a == 1:
        print("--------------查询余额----------------")
        print(f"顶针先生,您的余额为{x + 50000 - y}元")
        print("已退回主菜单")

    elif a == 2:
        # global x
        print("---------------存款----------------")
        x = eval(input("请输入存入的金额"))
        print(f"顶针先生,您已经存入{x}元,您现在余额为{x + 50000 - y}元")
    elif a == 3:
        # global y
        print("---------------取款--------------")
        y = eval(input("请输入取出的金额"))
        print(f"顶针先生,您已经取出{y}元,您现在余额为{x + 50000 - y}元")
    elif a == 4:
        print("已退出")
    else:
        print("您输出的程序错误,已自动退出")
def tab():
    print("--------------主菜单-----------------")
    print(f"{name}你好,欢迎来到瑞克专卖店,请选择您的会员卡服务:")
    print("查询余额\t[输入1]", end='')
    print()
    print("存款  \t[输入2]", end='')
    print()
    print("取款  \t[输入3]", end='')
    print()
    print("退出  \t[输入4]", end='')
    print()
    return find(eval(input("请输入你的选择:")))

name = input("客户您好,请输入您的名字")
i = False
while i == True:
    print(tab())
    if find(4):
        break
