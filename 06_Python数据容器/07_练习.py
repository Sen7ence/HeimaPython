string = 'itheima itcast boxuegu'
# 统计字符串内有多少个"it"字符
num = string.count('it')
print(num)

# 将字符串内的空格，全部替换为字符："|"
string = string.replace(' ', '|')
print(string)

# 并按照"|"进行字符串分割，得到列表
string_list = string.split('|')
print(string_list)
