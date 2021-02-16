#Assignment 26
#ฟีโบนัชชี (Fibonacci)

#0, 1, 1(0+1), 2(1+1), 3(2+1),.......

def fibonacci(number):
    if number<=1:
        return number        
    
    else:
        return fibonacci(number-1) + fibonacci(number-2) #ลำดับหลัง+ลำดับหน้า

for i in range(10): #0, 1, 2, 3, 4
    print(fibonacci(i)) #0,1,1,2,3,......