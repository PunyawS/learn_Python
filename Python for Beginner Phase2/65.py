#Assignment 25
#แฟกทอเรียล (Factorial)
"""5! = 5 x 4 x 3 x 2 x 1 = 120"""
def factorial(number):
    if number ==1:
        return number
    else:
        return number*(factorial(number-1))

x=factorial(5)
print(x)