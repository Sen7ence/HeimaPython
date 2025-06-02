# 定义列表
age_list = [21, 25, 21, 26, 22, 20]

# 增加31到列表尾部
age_list.append(31)
print(age_list)

# 增加列表[29,33,30]到尾部
age_list.extend([29, 33, 30])
print(age_list)

# 取出第一个元素
num0 = age_list[0]
print(age_list)

# 取出最后一个元素
num1 = age_list[-1]
print(age_list)

# 查找元素31在列表中的下标
index = age_list.index(31)
print(index)
