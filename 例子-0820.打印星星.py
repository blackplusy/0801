#coding=utf-8
#range()
#菱形

for i in range(-3,4):
    #print(i)
    if i<0:
        a=-i
    else:
        a=i
    print(' '*a+'*'*(7-a*2))
    
#对顶三角形
n=7
e=n//2
#             -3,4
for i in range(-e,n-e):
    a=-i if i<0 else i
    #a==3
    #e==3
    print(' '*(e-a)+'*'*(2*a+1))
    
