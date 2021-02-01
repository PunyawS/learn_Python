#Assignment 10
#หาผลรวมและค่าเฉลี่ยโดยใช้ Loop while

start = int(input("Ples input start :"))
stop = int(input("Ples input end :"))
sumation = 0
avgrage = 0

while start<=stop:
    number=int(input("Ples input number :"))
    sumation+=number
    start+=1
avgrage=sumation/stop
print("Sumation is :",sumation,"\n","Average is :",avgrage)