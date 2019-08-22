#coding=utf-8

#单继承

class dog:
    def __init__(self,name,color='black'):
        self.name=name
        self.color=color
    def run(self):
        print('狗富贵，互相旺！！')

class taidi(dog):
    def set_name(self,name):
        self.name=name
    def eat(self):
        print('im eating!!!')

gou=taidi('tai tan')

print('名字为%s'%gou.name)

gou.eat()

gou.set_name('2ha')

print('旺财的心名字',gou.name)

gou.run()


#多继承
class mom:
    def print_a(self):
        print('大眼睛')
class dad:
    def print_b(self):
        print('双眼皮')
class baby(mom,dad):
    def print_c(self):
        print('个子高高')

c=baby()
c.print_a()
c.print_b()
c.print_c()


#父类重写
class dog:
    def sayhi(self):
        print('wang!!!')

class fadou(dog):
    def sayhi(self):
        print('aowu~~~~~~')

dog1=fadou()
dog1.sayhi()







        



















