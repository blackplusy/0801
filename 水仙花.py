#coding=utf-8
a=int(input('输入一个三位数>>'))
#a=153
#百位
bai=a//100

#十位
shi=a%100//10

#个位
ge=a%10

if bai**3+ge**3+shi**3==a:
    print('水仙花')
else:
    print('not 水仙花')




