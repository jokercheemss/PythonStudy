zi = "团长你就是个及,麻你测我"
wo = zi[::-1][0:4]
print(wo)


worker1 = {"name": "顶针", "key": "瑞克部","工资": "3000", "级别": 1}
worker2 = {"name": "孙小船", "key": "贴吧部","工资": "5000", "级别": 2}
worker3 = {"name": "陈瑞", "key": "避战部", "工资": "7000", "级别": 3}
print("全体员工信息如下:")
print(worker1)
print(worker2)
print(worker3)

if worker1["级别"] == 1:
    worker1["工资"] += 1000
    print(worker1)

