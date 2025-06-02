# 黑马ATM

#定义全局变量money name
money = 5000000

# 客户输入姓名
name = input("请输入您的姓名：")

# 定义查询函数
def query(show_header): #利用show_header变量控制抬头的产生与否，以便在存款、取款函数中调用查询余额函数
    if show_header:
        print('----------查询余额----------')
    print(f'{name}，您好，您的余额剩余：{money}元')

# 定义存款函数
def saving(num):
    global money
    money += num
    print('----------存款----------')
    print(f'{name}，您好，您存款{num}元成功')
    query(False)

# 定义取款函数
def get_money(num):
    global money
    money -= num
    print('----------取款----------')
    print(f'{name}，您好，您存款{num}元成功')
    query(False)

# 定义主菜单函数
def main():
    print('----------主菜单----------')
    print(f'{name}，您好，欢迎来到黑马银行ATM。请选择操作：')
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return input('请输入您的选择：')
# 设置无限循环，确保程序不退出
while True:
    choice = main()
    if choice == '1':
        query(True)
    elif choice == '2':
        saving(int(input('请输入您的存款金额：')))
    elif choice == '3':
        get_money(int(input('请输入您的取款金额：')))
    else:
        print('已退出程序')
        break