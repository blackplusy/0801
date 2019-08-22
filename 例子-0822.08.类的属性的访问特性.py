#coding=utf-8

class test:
    a=100                   #类的属性
    def __init__(self,b):
        self.b=b            #实例属性

t=test(998)     #实例化对象
#1.通过实例化对象访问类的属性
print('t.a=%d'%t.a)

#2.通过类名访问类的属性
print('test.a=%d'% test.a)

#3.通过实例化对象访问实例属性
print('t.b=%d'%t.b)

#通过类名访问实例属性
print('test.b=%d ' %test.b)
