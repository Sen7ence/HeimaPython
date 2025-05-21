class Student:
    name = None

    def say_hi(self):
        print("hello 大家好")

    def say_hi2(self, msg):
        print(f"大家好，{msg}")


stu = Student()
stu.say_hi()
stu.say_hi2("很高兴认识大家")
