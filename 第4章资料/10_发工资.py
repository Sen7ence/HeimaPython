import random
money=10000
for i in range(1,21):
    score=random.randint(1,10)
    if score<5:
        print(f'员工{i}绩效分{score}，低于5，不发工资，下一位。')
        continue
    else:
        money-=1000
        print(f'向员工{i}发放1000元工资，账户余额还剩{money}元')
        if money==0:
            print('工资发完了')
            break