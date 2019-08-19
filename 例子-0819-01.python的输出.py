#coding=utf-8
'''
#coding=utf-8 设置字符集
字符集相当于翻译官，解析不同的语言用于显示
中国的字符集：GBK2312
'''
'''
1.直接输出
'''
#直接输出是通过print()函数进行打印
#输出翻滚吧牛宝宝！！！

print("翻滚吧牛宝宝")


'''
2.变量输出
'''
#变量可以理解为容器，容器的值是不固定的，设置什么保存什么
name='python'
print(name)

#变量之间也可以进行操作
a=20
b=30
print(a+b)
a='heygor is '
b='handsome!!! '
print(a+b)

'''
3.函数输出
'''
#输出通过函数处理过的值
#abs()    绝对值
#len()    字符串的长度
print(abs(-20))
name='heygorgaga'
print(len(name))

'''
格式化输出
'''
#  %s  输出字符串
#  %d  输出整型
#如果说语句中只传入一个变量，不用加括号，如果是多个变量需要加括号
name='python'
no=1
print('%s is no.%d'%(name,no))

name='heygor'
print('%s is sososo handsome!!!'% name )

#print('%d is good'% name)







