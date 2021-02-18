# การระบุชื่อ Exception ใน Except
#-------------------------------------------#
#ValueError => ใส่ค่าผิดพลาด
#ZeroDivisionError => ใช้ 0 เป็นตัวหาร

try:
    x=int(input("Ples input number :"))
    y=int(input("Ples input number :"))
    sum=x/y
    print(sum)
except ValueError:
    print("Use number")
except ZeroDivisionError:
    print("Use other number")
except TypeError:
    print("Type not match")