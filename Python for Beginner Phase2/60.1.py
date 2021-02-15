#e.g. programe Function return
import random

number = random.randrange(0,999)
def randomnumber(x):
    if x == number:
        print("Yes")
        return 1000
    else:
        print("No")
        return 0

money=randomnumber(int(input("Ples input :")))
print(money)