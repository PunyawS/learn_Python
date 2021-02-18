#Try..Except..Else
try:
    x=int(input("Ples input number :"))
    y=int(input("Ples input number :"))
    sum=x/y
    print(sum)
except Exception as a:
    print(a)
else:
    print("End Process.")