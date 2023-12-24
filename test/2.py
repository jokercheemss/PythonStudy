class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        def show(self):
            print(self.name+','+self.gender+','+self.age,end=",")
class Student(Person):
    def __init__(self,no,name,gender,age,major):
        Person(self,name,gender,age)
        self.no = no
        self.major = major
    def show(self):
        print(self.no,end=",")
        Person.show(self)
        print(self.major,end="\n")
class StudentList:
    def __init__(self):
        self.student = []
        def __insert(self,student):
            i = 0
            while(i<len(self.student)and s.sno>self.students[i].sno):
                i+=1
            if i<len(self.student)and s.sno == self.students[i].sno :
                print(s.sno+"已经存在")
                return False
            self.student.insert(s)
            print("增加成功")
            return True
        def __update(self,s):
            flag = False
            len = len(self.students)
            for i in range(len):
                if s.sno == self.student[i].sno:
                    self.student[i].name = s. name
                    self.student[i].gender = s.gender
                    self.student[i].age = s.age
                    self.student[i].major = s.major
                    print("修改成功")
                    flag = True
                    break
            if not flag :
                print("没有这个学生")
            return flag
        def __delete(self,sno):
            flag = False
