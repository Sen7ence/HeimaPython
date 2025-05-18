"""
演示Python的模块导入
"""

# 使用import导入time模块使用sleep函数
# import time
# print("开始")
# time.sleep(3)  # 暂停3秒 使用模块的内置功能：类、函数、变量等
# print("结束")

# # 使用from导入time模块的sleep函数
# from time import sleep  # 只导入sleep函数
# print("开始")
# sleep(3)  # 暂停3秒 直接使用sleep函数
# print("结束")

# # 使用*导入time模块的所有函数
# from time import *  # 导入time模块的所有函数 *表示全部
# print("开始")
# sleep(3)  # 暂停3秒 直接使用sleep函数 不用写time.前缀
# print("结束")

# # 使用as给模块起别名
# import time as t  # 给time模块起别名为t
# print("开始")
# t.sleep(3)  # 暂停3秒 使用别名调用模块中的函数
# print("结束")

# # 使用as给函数起别名
# from time import sleep as s  # 给sleep函数起别名为s
# print("开始")
# s(3)  # 暂停3秒 使用别名调用函数
# print("结束")
