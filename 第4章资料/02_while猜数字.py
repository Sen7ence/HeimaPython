# 获取范围在1-100的随机数字
import random
num = random.randint(1, 100)

#获取猜的数字
guess_num = int(input('输入要猜的数字：'))

#定义猜测次数
count=1

while guess_num != num:
    if guess_num > num:
        guess_num = int(input('猜大了，再猜一次：'))
    else:
        guess_num = int(input('猜小了，再猜一次：'))
    count+=1
else:
    print(f'猜对了！你的猜测次数是：{count}')