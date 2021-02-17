#Assignment 27
#ฟังก์ชั่นหาผลรวม & ค่าเฉลี่ยตัวเลข

def summation(number):
    total,avg=0,0
    for i in number:
        total+=i
    avg=total/len(number)
    return total,avg
    

x=[1,2,3,4,5,6,7,8]
total,sum=summation(x)
print("Total :",total,"\nSummation :",sum)