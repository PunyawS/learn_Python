# เจาะลึก Return
import random

number = random.randrange(0,999)
def randomnumber(x):
    if x < 0 or x > 999:
        return # หาก x เข้าเงื่อนไขจะกระโดดออกจาก Function
    if x == number:
        print("Yes")
        return 1000
    else:
        print("No")
        return 0

money=randomnumber(int(input("Ples input :")))
print("รางวัล :",money)