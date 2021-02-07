#Assignment 17

number=[]
while True:
    x=int(input("Ples input number :"))
    if x<0:
        break
    number.append(x)
number.sort()
print(number)
number.reverse()
print(number)

print("Min is :",min(number))
print("Max is :",max(number))
print("Sum is :",sum(number))
print("End Process")