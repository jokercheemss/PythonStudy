try:
    file = open("D:\demo.txt", "rt")
    print("把文件打开")
    file.cslose()
    file = open("D:\demo.txt", "wt")
    file.write("忘不了的人")
    file.close()
except:
    print("文件打开失败")



def writrework():
    try:
        file = open("D:\demo.txt", "wt")
        file.write("j\n忘不了的人")
        file.close()
    except:
        print("写文件失败")

def read():
    try:
        file = open("D:\demo.txt", "rt")
        s = file.read()
        print(s)
        file.close()
    except:
        print("写文件失败")





