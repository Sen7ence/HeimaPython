# 定义元组
stu = ('周杰轮', 11, ['football', 'music'])

num = stu.index(11)
print(num)

print(stu[1])

del stu[2][0]
print(stu)

hobby = stu[2]  # 不是对列表的拷贝，而是对列表的引用，同一个对象
hobby.append('coding')
print(stu)
