# -*- codeing = utf-8 -*-
# @Time :2022/4/3 15:23
# @Author:刘伟怡
# @File :demo3.py
# @Software :


# str="chengdu"
# print((str+'\t')*3)


# sentence="你狗日的fuck你"
# filter_sentence=sentence.replace("狗日的","***").replace("fuck","*")
# import datetime
# now=datetime.datetime.now()
# print(filter_sentence,"|",now)

'''
a=[0,2,3]
a.insert(1,5)
print(a)'''

'''moveName=["aaa","bbb","ccc"]
for name in moveName:
    print(name)
# del moveName[2]
# moveName.pop()
moveName.remove("bbb")
print("========================")
for name in moveName:
    print(name)'''

# nameList=["aaa","bbb","ccc"]
# nameList[1]="ppp"
# findName=input("请输入查找姓名:")
# if findName in nameList:
#     print("找到了")
# else:
#     print("没有")
'''
a=["a","b","a","d","a","b"]
print(a.index("a",1,4))
print(a.count("c"))
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
'''

# schoolName=[["北京大学","清华大学"],["清华大学"],["天津大学"]]
#
# print(schoolName[0][0])

'''
import random
offices=[[],[],[]]
teacher=["A","B","C","D","E","F"]
for name in teacher:
    index=random.randint(0,2)
    offices[index].append(name)
i=1
for temName in offices:
    print("办公室%d人数%d"%(i,len(temName)))
    i=i+1
    for name in temName:
        print(name,end=' ')
    print()
    '''

produce=[["iphone",6888],["MacaPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("-------------  商品列表  -------------")
print(" 0    iphone     6888\n",'1    MacaPro    14800\n',"2    小米6       2499\n","3    Coffee     31\n",
      "4    Book       60\n","5    Nike       699\n")
buy=[]

aa=input("您想要买什么，请输入列表序号:")
if aa=='q':
   print("成功推出")
else:
    while aa!='q':
        aa=input("您想要买什么，请输入列表序号:")
        if aa=='q':
            break
        else:
            buy.extend(aa)
print("您加入购物车的商品是：",buy)






















