# 接受传入文件的路径，打印文件的全部内容，文件不存在则捕获异常，通过finally语句关闭文件对象
def print_file_info(file_name):
    try:
        open_file = open(file_name, 'r', encoding='utf-8')
        print(open_file.read())
    except FileNotFoundError:
        print("文件不存在，请检查文件路径是否正确！")
    finally:
        if open_file:
            open_file.close()


# 接受文件路径及传入数据，将数据追加写入到文件中
def append_to_file(file_name, date):
    try:
        open_file = open(file_name, 'a', encoding='utf_8')
        open_file.write(date)
        open_file.close()
    except FileNotFoundError:
        print("文件不存在，请检查文件路径是否正确！")
