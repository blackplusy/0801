#coding=utf-8

dic={'simida':'123','kouniqiwa':'456'}

while 1:
    name=input('请输入用户名')
    if name in dic.keys():
        print('用户名正确')
        while 1:
            passwd=input('请输入密码')
            if passwd==dic[name]:
                print('输入密码正确')
                print('您已经登录')
                break
            else:
                print('密码不匹配，请重新弄输入')
        break
    else:
        print('用户名输入错误,请重新输入用户名')

