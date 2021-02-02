#assignment 13

"""
xxxyyyxxx
xxxyyyxxx
xxxyyyxxx

x= black
o= white
"""
last = int(input("size :"))
for row in range(last):
    for column in range(last): 
        print ("x",end='') if (row+column) %2 ==0 else print("o",end='')
    print("")

# size = 4 x 4
# row = 0 + column = 0  x
# row = 0 + column = 1  o
# row = 0 + column = 2  x
# row = 0 + column = 3  o

# row = 1 + column = 0  o
# row = 1 + column = 1  x
# row = 1 + column = 2  o
# row = 1 + column = 3  x

"""
xoxo
oxox
"""