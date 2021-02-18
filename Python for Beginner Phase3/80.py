# สร้าง Exception ด้วย Raise

while True:
    try:
        name=str(input("Ples input your name :"))
        if name == "kk":
            raise Exception("มีผู้ใช้แล้ว")
    
        x=int(input("Ples input number :"))
        y=int(input("Ples input number :"))
        if x == 0 and y == 0:
            break
        if x<0 or y<0 :
            raise Exception("ป้อนค่าติดลบไม่ได้")
        result=x/y
        print(result)
    except Exception as a:
        print(a)