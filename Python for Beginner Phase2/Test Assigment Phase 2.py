""" def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number-1)+fib(number-2)

for i in range(5):
    print(fib(i))
 """

""" def hanoi(n,a,b,c):
    if n==0:
        return
    hanoi(n-1,a,c,b)
    print("จานที่",n,"จาก",a,"ไป",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C") """
