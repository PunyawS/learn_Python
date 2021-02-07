#Assignment 18
#หากลุ่มเลขคู่และคี่
number=[]
odd=[] #คี่
even=[] #คู่
while True:
    x=int(input("Ples input number :"))
    if x<0:
        break
    number.append(x)
    if x %2==0:
        odd.append(x)
    else:
        even.append(x)
print(odd)
print(even)
number.sort()
print(number)
number.reverse()
print(number)
print(max(number))
print(min(number))
