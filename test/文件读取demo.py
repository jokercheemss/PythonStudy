a = open("D:\demo.txt","w",encoding="ANSI")
a.write("我不会忘忘了你的")
a.write("我不会忘忘了你的")
a.flush()
a.close()



message = open("D:/test.txt","w",encoding="ANSI")
type1 = "正式"
type2 = "测试"

message.write(f"周杰伦  2022-01-01 1000 {type1}\n")
message.write(f"刘德华  2022-01-02 1000 {type2}\n")
message.write(f"柴浩啊  2022-01-03 1000 {type1}")



message.flush()
message.close()