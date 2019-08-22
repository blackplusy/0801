#coding=utf-8
#加法
sum=lambda a1,a2:a1+a2

print(sum(10,20))

#字典排序
stu=[{'name':'tom','age':18},{'name':'jerry','age':20},{'name':'snoopy','age':16}]
stu.sort(key=lambda x:x['age'])
print(stu)

#把lambda当做变量使用
def operation(a,b,opt):
    re=opt(a,b)
    return re

num1=int(input('num1'))
num2=int(input('num2'))

res=operation(num1,num2,lambda a,b:a+b)
print(res)
