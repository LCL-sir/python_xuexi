# 构造方法在实现类的时候 自动执行
class Student:
    name: None
    age: None

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("小明", 18)

print(student.name)
print(student.age)
