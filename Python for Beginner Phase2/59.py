#List Parameter

def displaynumber(number):
    print(number)
    for i in number:
        print("เลขที่ :",i)

def displaynum(num):
    print(num)
    for i in num:
        print("เลขที่ :",i)

number=[1,2,3,4,5] #List
num=(1,2,3,4,5) #Tuple
displaynumber(number)
displaynum(num)