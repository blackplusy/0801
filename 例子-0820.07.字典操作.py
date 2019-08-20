#coding=utf-8

#创建字典
dic={'name':'哪吒','age':18}

#访问字典
print(dic)
#筛选数据
print(dic['age'])


#del删除字典
dic={'name':'5kong','password':'123'}
print(dic)

del dic['name']
print(dic)

del dic
#print(dic)

#clear清空字典

dic={'name':'5kong','password':'123'}
print(dic)
dic.clear()
print(dic)

#字典的修改
dic={'name':'5kong','password':'123'}
print(dic)
dic['name']='shasir'
print(dic)
dic['age']=110
print(dic)

#keys
dic={'name':'5kong','password':'123'}
print(dic.keys())
for i in dic.keys():
    print(i)

#values
dic={'name':'5kong','password':'123'}
print(dic.values())
for i in dic.values():
    print(i)

#items
for a,b in dic.items():
    print(a,b)
















