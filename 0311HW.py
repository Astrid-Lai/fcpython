# -*- coding: utf-8 -*-
"""
2021.03.11 Python作業
學員105276677  賴昱辰

"""

#1.請隨機取數，1~49取6個，且整數不可重複，並放入串列

import random
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
print( random.sample(number, k=6) )





#2.[100,80,1,3,10,7]，請排序小到大

number=[100,80,1,3,10,7]

a=[100,80]
a.reverse()
number[0]=a[0]
number[1]=a[1]

b=[100,1]
b.reverse()
number[1]=b[0]
number[2]=b[1]

c=[80,1]
c.reverse()
number[0]=c[0]
number[1]=c[1]

d=[100,3]
d.reverse()
number[2]=d[0]
number[3]=d[1]

e=[80,3]
e.reverse()
number[1]=e[0]
number[2]=e[1]

f=[100,10]
f.reverse()
number[3]=f[0]
number[4]=f[1]

g=[80,10]
g.reverse()
number[2]=g[0]
number[3]=g[1]

h=[100,7]
h.reverse()
number[4]=h[0]
number[5]=h[1]

i=[80,7]
i.reverse()
number[3]=i[0]
number[4]=i[1]

j=[10,7]
j.reverse()
number[2]=j[0]
number[3]=j[1]
print(number)
print()