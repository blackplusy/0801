#coding=utf-8
'''
class people:
    country='China'
    @classmethod
    def getcountry(cls):
        return cls.country

p=people()

print(p.getcountry())   #通过实例化对象调用类的方法
print(people.getcountry())#通过类对象调用类的方法

'''

class people:
    country='China'
    @classmethod
    def getcountry(cls):
        return cls.country
    @classmethod
    def setcountry(cls,country):
        cls.country=country

p=people()

print(p.getcountry())

p.setcountry('peoples republic of china')

print(p.getcountry())
