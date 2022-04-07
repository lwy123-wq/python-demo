# -*- codeing = utf-8 -*-
# @Time :2022/4/6 14:52
# @Author:刘伟怡
# @File :demo7.py
# @Software :
import datetime

printName=input("请输入您的名字：")
print("%s欢迎您的到来"%printName)
try:
    f=open("guest_book.txt","w",encoding='utf-8')
    while True:
        sum=input("请输入语句如果想关闭请按q:")
        time=str(datetime.datetime.now())
        if sum=='q':
            break
        f.write(printName+"说："+sum+"当前时间为："+time+'\n')
except Exception as result:
    print(result)
finally:
    f.close()
    print("文件已关闭")
