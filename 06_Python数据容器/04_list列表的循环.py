"""
演示使用while和for循环遍历列表
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认0
    index = 0
    while index < len(mylist):
        # 通过下标索引来访问列表元素
        print(mylist[index])
        # 每一次循环将下标索引加1
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: 
    """
    mylist = [1, 2, 3, 4, 5]
    for i in mylist:
        print(i)


list_while_func()
list_for_func()
