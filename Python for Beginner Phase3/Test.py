""" def fib(number):
    if number<=1:
        return number
    else:
        return fib(number-1)+fib(number-2)

x=int(input(":"))
for i in range(x):
    print(fib(i)) """
    

""" def fact(number):
    if number==1:
        return number
    else:
        return number*(fact(number-1))

x=int(input(":"))
print(fact(x))
 """

""" def sumation(number):
    total,avg=0,0
    for i in number:
        total+=i
    avg=total/len(number)
    return total,avg

x=[1,2,3,4,5,6,7,8]
total,avg=sumation(x)
print(total,avg) """




