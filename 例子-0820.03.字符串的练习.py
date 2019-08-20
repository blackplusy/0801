#coding=utf-8
a=input('请输入字符串>>')
'''
if a=='':
    print('为空！')
'''

'''
if len(a)==0:
    print('为空')
elif a[0]=='A' or  a[0]=='E':
    print('yes')
else:
    pass
'''

if len(a)==0:
    print('null')
elif a[0] in 'aeiouAEIOU':
    print(a+'ay')
else:
    print(a[1:]+a[0]+'ay')
