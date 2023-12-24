b = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天")
w = int(input("请输入1到7的数字"))
if 0 < w <= 7:
    print("你输入是", b[w-1])
else:
    print("错误")
#######################
def max(*args):
    print(args)
    m = args[0]
    for i in range(len(args)):
        if m < args[i]:
            m = args[i]
    return m

print(max(1, 2))
print(max(1, 2, 0, 3))
###################
def fun (x, y=2, *args, **kargs):
    print(x,y)
    print(args)
    print(kargs)
fun(1, 2)
fun(1, 2, 3, 4)
fun(1, 2, 3, 4, z=5, s="demo")



#英语字典

sum = {'word': '单词', '张': '是个嘚', 'bqs': '123', '666': '好耶！'}

def xianshi():   #显示
    print(sum)
    return sum

def chazhao():   #查找
    a = input("请输入单词：")
    print("解释：", sum[a])

def shanchu():   #删除
    a = input("请输入要删除的单词：")
    del sum[a]
    print("删除完毕！")

def zengjia():   #增加
    a = input("请输入要增加的单词：")
    b = input("单词的注解：")
    sum[a]=b
    print("单词增加完毕！")

def gengxing():   #更新
    a = input("请输入要更新的单词：")
    b = input("更新为：")
    sum[a]=b
    print("更新完毕！")
print("1.显示 2.查找 3.增加 4.删除 5.更新 6.退出")
while True:
    try:
        s = input("请输入指令：")
        s = int(s)
        if s == 1:
            print("显示：")
            xianshi()
        elif s == 2:
            print("查找：")
            chazhao()
        elif s == 3:
            print("增加：")
            zengjia()
        elif s == 4:
            print("删除：")
            shanchu()
        elif s == 5:
            print("更新：")
            gengxing()
        elif s == 6:
            print("程序退出！")    #退出
            break
    except Exception as err:
        print("查无此词！")
