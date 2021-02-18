#Try...Except ทำงานร่วมกับ While

while True:
    try:
        x=int(input("Ples input number :"))
        y=int(input("Ples input number :"))
        if x == 0 and y == 0:
            break
        result=x/y
        print(result)
    except Exception as a:
        print(a)
    finally:
        print("On process.")
        