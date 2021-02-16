def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number-1)+fib(number-2)

for i in range(5):
    print(fib(i))
