#assignment 16
#รับและเรียงลำดับข้อมูลตัวเลข

number=[]
while True:
    x=int(input("Input your number :"))
    if x<=0:
        break
    number.append(x)

number.sort()
print(number)
number.reverse()
print(number)
print("End Process")