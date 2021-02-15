# Function return
""" 
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการรับค่าเข้าไปทำงาน
def name(a,b): #*args เช่นกัน

3. รับค่าเข้าไปทำงาน และส่งออกมาเพื่อนำไปใช้งานที่โปรแกรมหลัก
def name(a,b):
    return a+b

4. ไม่มีการรับค่าเข้ามาแต่ส่งค่าออกไป
def number():
    return
"""

def add(a,b):
    return a+b

def number():
    return 500

y=number()
print(y)
x=add(10,20)
print(x)
