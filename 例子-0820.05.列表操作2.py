#coding=utf-8

l=['a','b','c']
l.insert(1,'d')
print(l)
l.insert(-1,'aaa')
print(l)


l1=[1,2,3,4]
l1.extend('a')
print(l1)
l1.extend([1,2])
print(l1)

print(l1.index(3))

#栈方式访问列表
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)

#enumerate

for index,value in enumerate(l):
    print('索引是'+str(index)+',值是：'+str(value))


#列表的排序

l=[1,3,2,4]
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
l.sort()
l.reverse()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)


#列表推导式
#给定列表
a=[1,2,3,4]
print([5*x for x in a])

#没有给定列表可以使用range方法
print([3*x for x in range(1,11)])

#加入if条件进行推导
print([x for x in a if x%2==0])

#多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])















    



