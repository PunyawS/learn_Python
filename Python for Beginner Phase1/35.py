#assignment 14
#สร้างขอบตาราง
""" 
xxxx
x  x
x  x
xxxx
"""

last = int(input("input :"))
for i in range(last):
    for y in range(last):
        if i == 0 or i==last-1 or y==0 or y==last-1:
            print("x",end='')
        #elif i %2!=0 or i %2==0:
            #print("o",end='')
        else:
            print(" ",end='')
    print(" ")