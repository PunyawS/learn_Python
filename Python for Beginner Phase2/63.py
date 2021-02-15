#Function use Function

def equal(x,y,z):
    #Function use function
    #a=comparemax(x,y)
    #b=comparemax(a,z)
    #return b"""
    return comparemax(comparemax(x,y),z)

def comparemax(x,y):
    if x > y:
        return x
    else:
        return y



max=equal(10,20,-30)
print("Max :",max)