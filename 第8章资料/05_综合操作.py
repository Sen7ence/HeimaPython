fr = open(r'C:\Users\asus\Desktop\PythonLearning\HeimaPython\第8章资料\bili.txt',
          'r', encoding='UTF-8')

fw = open(r'C:\Users\asus\Desktop\PythonLearning\HeimaPython\第8章资料\bili.txt.bak',
          'w', encoding='UTF-8')

for line in fr:
    line = line.strip()     # 去除开头和结尾的空格以及换行符
    words = line.split(',')
    if words[4] == '测试':
        continue
    fw.write(line)
    fw.write('\n')

fw.close()
fr.close()
