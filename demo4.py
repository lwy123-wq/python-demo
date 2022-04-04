# -*- codeing = utf-8 -*-
# @Time :2022/4/4 14:17
# @Author:刘伟怡
# @File :demo4.py
# @Software :

'''tup1=(12,23,34)
tup2=("sss","sss","kkk")
print(tup2+tup1)'''
# 增
info = {"name": "aaa", "age": 12}
# newID=input("请输入新的学号：")
# info["id"]=newID
# print(info)

# 删
'''del info["name"]
print(info)'''
# 改

info["age"] = 30
print(info)
# 查
'''
print(info.keys())
print(info.values())
print(info.items())
for key,value in info.items():
    print(key,value)'''

# list=["a","b","c","e","d"]
# for i,list1 in enumerate(list):
#     print(i,list1)

# def printinfo():
#     print("--------------------")
# printinfo()

# def add2Num(a,b):
#     c=a+b
#     print(c)
# add2Num(1,4)

'''
def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu
sh,yu=divid(12,3)
print("商%d,余数%d"%(sh,yu))
'''


def printOneLine():
    print("-" * 30)


#printOneLine()

def printNumLine(num):
    i=0
    while i<num:
        printOneLine()
        i=i+1

#求三个数的和
def sum(a,b,c):
    return a+b+c

def average(a,b,c):
    sum=sum(a,b,c)
    result=sum/3
    return result
