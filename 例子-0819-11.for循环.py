#coding=utf-8

#字符串
for i in 'abcd':
    print(i)


#列表
l=[1,2,'simida','gaga']

for i in l:
    print(i)

#函数
#range函数
#range(10)   0-9
#range(1,10) 1-9

print('--------')
for i in range(10):
    print(i)

print('--------')
for i in range(1,10):
    print(i)

print('--------')
for i in range(-5,5):
    #print(i)
    if i<0:
        print(-i)
    else:
        print(i)
