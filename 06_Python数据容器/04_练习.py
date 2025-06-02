# 定义一个列表，内容是：[1,2,3,4,5,6,7,8,9,10]
# 遍历列表，取出列表内偶数，并存入一个新的列表对象

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = []
# while循环
i = 0
while i < len(mylist):
    if mylist[i] % 2 == 0:
        newlist.append(mylist[i])
    i += 1
print(newlist)

# for循环
newlist2 = []
for i in mylist:
    if i % 2 == 0:
        newlist2.append(i)
print(newlist2)
