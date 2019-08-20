#coding=utf-8
#列表的访问
l=['李元芳','李白','程咬金','猪八戒']

#直接访问
print(l)

#遍历访问
for i in l:
    print(i)

#成员判断
if '张小敬' in l:
    print('12时辰')
else:
    print('不在里面')

#列表的索引和切片
l1=['张飞','马超','云云','黄忠','刘备']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])


#列表的拼接
l1=[1,2,3,4]
l2=['heygor','baigor']
print(l1+l2)

#列表的更新
l=[1,2,3]
print(l)
l[2]='memeda!!!'
print(l)
l[-2]='柳岩'
print(l)

#列表的删除
l=[1,2,3,4]
print(l)
del l[2]
print(l)
del l
print(l)











