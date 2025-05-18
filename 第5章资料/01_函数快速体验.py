"""
演示：快速体验函数的开发及应用
"""
# 需求，统计字符串的长度，不使用内置函数len()

str1="欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！"
str2="体温测量中，您的体温是：37.3度，体温正常请进！"

def my_len(name):
    count = 0
    for i in name:
        count += 1
    print(f'字符串"{name}"的长度是{count}')

my_len(str1)
my_len(str2)