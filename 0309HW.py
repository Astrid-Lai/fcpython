# -*- coding: utf-8 -*-
"""
2021.03.09  Python作業
學員105276677  賴昱辰
"""

"""
1.做出此排列
123456789
12345678
1234567
123456
12345
1234
123
12
1
"""

for i in range(10,1,-1):
    for x in range(1,i):
        print(x,end="")
    print()


"""
2.做出下圖排列
   *
  ***
 *****
*******
 *****
  ***
   *
"""

for i in range(2,9,2):
    for x in range(1,i):
        print(x,end="")
    print()

for i in range(6,0,-2):
    for x in range(1,i):
        print(x,end="")
    print()    
    
    
    