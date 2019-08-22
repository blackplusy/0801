#coding=utf-8

class student:                     #创建一个类
    def study(self):               #方法列表
        print('im study!!')
    def play(self):
        print('play ball')

boy=student()
#产生一个student对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性，注意：后面如果再次出现，表示对属性的修改
boy.favor='game'
#给对象添加属性
boy.study()
#通过实例对象调用类的方法
boy.play()

print(boy.age)
print(boy.favor)
