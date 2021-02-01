# Loop in loop

i = 1
""" while i<=3:
    print("round :",i)
    j=1
    while j<=5:
        print("position :",j)
        j+=1
    i+=1 """

for i in range(1,4):
    print("Round :",i)
    for j in range(1,6):
        print("Position :", j)