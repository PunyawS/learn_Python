#อ่าน Text ไฟล์
#open("name","mode",การเข้ารหัส)

try:
    f = open('./Text/test.txt','r',encoding="UTF-8")
    s = f.readlines()
    for i in s:
        print(i)
    f.close()
except FileNotFoundError:
    print("File not found.")