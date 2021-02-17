#Assignment 27
#ฟังก์ชั่นนับอักษรตัวเล็กตัวใหญ่

def checkstring(message):
    result={"UPPER":0,"LOWER":0}
    for i in message:
        if i.isupper():
            result["UPPER"]+=1
        else:
            result["LOWER"]+=1
    return result


x=checkstring("ABccDE")
print(x)