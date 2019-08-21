#coding=utf-8
import csv
#读文件
with open('d:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)

#写文件
with open('d:\\2.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    file.writerow([4,5,6,7])
    file.writerow([4,4,4,4])

print('已经完成')
