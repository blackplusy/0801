#coding=utf-8
#读文件
file=open('D:\\1.txt','r')
#print(file)
for i in file:
    print(i)
file.close()


#写文件
str1='一切都是最好的安排'
file=open('D:\\2.txt','w')
file.write(str1)
file.close()
print('执行完毕')


#追加文件
file=open('D:\\2.txt','a')
file.write('\n come on baby!!!')
file.close()
print('追加完毕')
