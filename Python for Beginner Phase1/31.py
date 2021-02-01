# Find Mix&Min

while True:
    number1=int(input("input number :"))
    number2=int(input("input number :"))
    if number1<0 or number2<0:
        break
    elif number1 > number2:
        print("Max is :", number1,"\t","Mix is :",number2)
    elif number1 < number2:
        print("Max is :", number2,"\t","Mix is :",number1)
    elif number1 == number2:
        print(number1 ,"=", number2)
print("End process")