# เขียน Text ไฟล์

try:
    f=open('./Text/test.txt','w',encoding="UTF-8")
    f.write("Hello test1 text \n")
    f.writelines("Hello test2 text")
    f.close()
except Exception:
    print("File not found.")