#assingment 9
#แม่สูตรคูณ

start=int(input("ป้อนแม่สูตรคูณเริ่มต้น :"))
stop=int(input("ป้อนแม่สุดท้าย :"))

for x in range(start,stop+1):
    print("แม่ :",x)
    for y in range(1,13):
        ans=x*y
        print(x,"x",y,"=",ans)