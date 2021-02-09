number = int(input("ples input number :"))

for x in range(number):
    for y in range(number):
        #print("x",end='') if (x+y)%2==0 else print("o",end='')
    #print("")
        if x==0 or y==0 or x==number-1 or y==number-1:
            print("x",end='')
        else:
            print(" ",end='')
    print(" ")