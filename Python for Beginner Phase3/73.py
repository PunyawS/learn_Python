# Exception

# x=int(input("Ples input number :"))
# y=int(input("Ples input number :"))
# sum=x+y
# print(sum)
#-------------------------------------------#
""" 
try:
    คำสั่งรันโปรแกรมปกติ
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
"""
""" try:
    x=int(input("Ples input number :"))
    y=int(input("Ples input number :"))
    sum=x+y
    print(sum)
except ValueError:
    print("Program Error") """
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