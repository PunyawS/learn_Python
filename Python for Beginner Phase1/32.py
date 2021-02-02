#Assignment 11
#ตัวเลขขั้นบันได
""" 
1
12
123
1234
12345
123456
1234567 """

last=int(input("input your number :"))

for row in range(1,last+1): #กำหนดแนวตั้ง
    for column in range(1,row+1): #กำหนดแนวตั้ง
        print(column,end='')
    print("") 

""" 
input 4 
row = 1,4+1 (star at 1, end at 4)
column = 1,1+1  (show 1)

row = 2,4+1
column = 1,2+1 (show 12)

row = 3,4+1
column = 1,3+1 (show 123)

row = 4,4+1
column = 1,4+1 (show 1234) """