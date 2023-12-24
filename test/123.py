strline = str(input("输入一串字符"))
for i in range(1, len(strline) - 2):
    x = strline[i]
    y = strline[i + 1]
    z = strline[i + 2]
    if x == y and y == z and x == z:
        print("true")
        break
    else:
        print("false")


