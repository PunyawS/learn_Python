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
print("End Process")