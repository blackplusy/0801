#coding=utf-8

file=open('D:\\3.txt','r')
for i in file.readlines():
    #print(i)
    #print(type(i))
    i=i.strip('\n')
    a=i.split(' ')
    #print(a)
    if a[-1]=='110':
        print('110 is here!!!')
    
#    if '110' in i:
#        print('yes')
file.close()

'''
创建文件txl，内容为用户名字和电话
1.键盘输入用户名，判断是否存在文件中，如果
存在于文件中，直接输出对应电话，如果用户
名在文件中没有找到，提示该用户没有找到，
提示输入电话，电话输入完毕后，新的用户和
电话写入到文件中
'''
