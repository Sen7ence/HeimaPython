# 开学了有一批学生信息需要录入，请设计一个类，记录学生的：姓名、年龄、地址
# 通过for循环配合input输入语句，并使用构造方法，完成学生信息的键盘录入
# 输入完成后，使用print语句完成信息的输出


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(10):
    print(f"当前录入第{i+1}个学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    address = input("请输入学生地址：")
    stu = Student(name, age, address)
    print(
        f"学生{i+1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】"
    )
