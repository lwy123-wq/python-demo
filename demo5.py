# -*- codeing = utf-8 -*-
# @Time :2022/4/4 15:57
# @Author:刘伟怡
# @File :demo5.py
# @Software :

import random

code = []
for i in range(65, 91):  # A-Z
    code.append(chr(i))
for j in range(97, 123):
    code.append(chr(j))
for k in range(48, 58):  # 0-9
    code.append(chr(k))
r_code = random.sample(code, 6)
rr_code = "".join(r_code)
print("随机验证码为:", rr_code)

# f = open("test.txt", "r")
#f.write("Hello I'm hungry")
# contest=f.readlines()
# print(contest)
# for i,name in enumerate(contest):
#     print(i,name)
# f.close()
