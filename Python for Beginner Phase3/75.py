# การเขียน Exception ใน except 
# ในกรณีที่ไม่ทราบชื่อ Exception ตรงไหน
try:
    x=int(input("Ples input number :"))
    y=int(input("Ples input number :"))
    sum=x/y
    print(sum)
except Exception as a:
    print(a)