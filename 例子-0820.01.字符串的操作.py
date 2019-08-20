#coding=utf-8

name='im your papa！'

#字符串的索引
print(name[0])
print(name[2])
print(name[-2])

#字符串的切片,左闭右开

print(name[0:4])

print(name[:4])

print(name[4:])

print(name[3:-1])


#字符串的拼接
a='lady'
b='gaga'
print(a+b)
print(a+b[0])

tel='0452-8869504'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])


#字符串遍历
for i in tel:
    print(i)

#去空格
#str.strip()   去掉两边空格
#str.lstrip()  去掉左边空格
#str.rstrip()  去掉右边空格
str1='   python   '
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

#计算长度6
#len() 计算元素个数
print(len(str1))


#引号操作
print('hey man whats up!')

print("looking for a girl")

#print('i'm your papa!')

print("i'm your mom!!")

print('''赛浪嘿哟！''')

print('''
name:heygor
tel:110
QQ:688
''')
'''
heygor 贼TM帅
'''










