#Recursive Function

def cat(x):
    if x==5:
        return
    print(x)
    x+=1
    cat(x)

def summation(x):
    if x==1:
        return x
    else:
        return x+summation(x-1) #summation(5-1=4, 4-1=3, 3-1=2, 2-1=1)
    
x=summation(5) #5+4+3+2
print(x)
