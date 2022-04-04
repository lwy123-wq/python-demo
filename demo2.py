# -*- codeing = utf-8 -*-
# @Time :2022/4/3 14:40
# @Author:刘伟怡
# @File :demo2.py
# @Software :

'''
i=0
while i<5:
    print("当前第%d次："%(i+1))
    print("i=%d"%i)
    i=i+1
    '''

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()








'''i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        pass
    print(i)'''


