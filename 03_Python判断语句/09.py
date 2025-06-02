#产生随机数
import random
num = random.randint(1,10)

guess_num=int(input('输入你猜的数：'))

if num==guess_num:
    print('恭喜你一次就猜对了！')
else:
    if num>guess_num:
        print('你猜的数小了')
    else:
        print('你猜的数大了')
    guess_num=int(input('再猜一次:'))
    if num==guess_num:
        print('恭喜你第二次猜对了！')
    else:
        if num>guess_num:
            print('你猜的数小了')
        else:
            print('你猜的数大了')
        guess_num=int(input('再猜一次:'))
        if num==guess_num:
            print('恭喜你第三次猜对了！')
        else:
            print('很遗憾，三次都没有猜对。')