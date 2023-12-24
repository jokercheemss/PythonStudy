# 函数的说明文档(注释)
def a(x, y):
    """
    :param x:指示灯真
    :param y:芝士雪豹
    :return:返回值为理塘
    
    """
    answer = x + y
    return answer


a(1, 2)




list = ["顶针","理塘","世界最高成"]
# 列表的位置
a = list.index("顶针")
# 列表的元素插入
list.insert(1, "雪豹")
# 列表元素的取代
list[0] = "雪豹"
print(a)
print(list)


last = [21, 25, 21, 23, 22, 20]
last.append(31)
print(last)
last1 = [29, 33, 30]
last.append(last1)
print(last)
last.remove(21)
print(last)
del last1[-1]
print(last)
a = last.index(31)
print(a)

x = 0
for i in range(len(last)):
    y = last[x]
    if i <= x:
        print(f"列表中元素是{y}")
    else:
        break
    x += 1









