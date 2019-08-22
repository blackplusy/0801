#coding=utf-8
import os
import sys
os.system('dir')            #运行系统中的命令
#os.remove('D:\\1.txt')     #删除系统中的文件
os.getcwd()                 #当前路径
print(os.listdir('D:\\'))   #查看指定目录下所有文件
print(os.path.split('D:\\mz\\2.txt'))  #返回一个路径的目录和文件名
print(os.path.isfile('D:\\2.csv'))     #判断是否是目录

print(sys.version)

print(sys.path)
