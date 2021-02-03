#assignment 15
#1,2,3,4,5,6

import random
myrandom = random.randrange(1,7)
k = 0
corrent = False
print("You have 5 chances")
while True:
    if k>=5:break
    number=int(input("Guess what ? :"))
    corrent=(number==myrandom)
    if number<=0:
        break
    if corrent:
        print("You are smart.")
        break
    else:
        print("Fucking idiot !"",""Try again loser")
        print("Number is smaller than Number Random")if number<myrandom else print("Number is greater than Number Random")
    k+=1

if not corrent:
    print("Number random is :",myrandom)
    
print("End process")