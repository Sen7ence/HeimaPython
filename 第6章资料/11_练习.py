# 信息去重
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
           'itheima', 'itcast', 'itheima', 'itcast']
my_set = set()

# for 循环遍历列表
for element in my_list:
    print(element)
    my_set.add(element)

print(my_set)
