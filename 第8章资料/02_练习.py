# f = open('C:\\Users\\asus\\Desktop\\PythonLearning\\HeimaPython\\第8章资料\\world.txt',
#          'r', encoding='UTF-8')
# a = 0
# for line in f:
#     line = line.strip()     # 去除开头和结尾的空格以及换行符
#     words = line.split(' ')
#     for word in words:
#         if word == 'itheima':
#             a += 1

# print(a)
# f.close()

with open('C:\\Users\\asus\\Desktop\\PythonLearning\\HeimaPython\\第8章资料\\world.txt') as f:  # 打开world.txt。r表示不对反斜杠进行转义
    a = 0
    for lines in f:  # 读取每行
        line = lines.strip()  # 使用strip()去除首尾空白
        words = line.split(' ')  # 使用split(' ')将每行按空格分词，存入列表
        for word in words:
            if word == 'itheima':
                a += 1
    print(a)

# 另一种思路利用f.read读取全部内容，利用.count()读取
