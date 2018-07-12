# csv：数据保存的格式，每个字段之间，以逗号分隔
# 它有头部

import csv

list = [
    {'name': '王', 'age': '10', },
    {'name': '张', 'age': '20', },
    {'name': '李', 'age': '30', },
]

csvfile = open('134.csv', 'w')
# csv文件的头
fieldnames = ['name', 'age']
writehandler = csv.DictWriter(csvfile, fieldnames)
# 写入头
writehandler.writeheader()
# 写入数据
writehandler.writerows(list)
csvfile.close()

# 读取csv文件
csvfile = open('134.csv', 'r')

reader = csv.reader(csvfile)
for line in reader:
    print(line)
csvfile.close()
