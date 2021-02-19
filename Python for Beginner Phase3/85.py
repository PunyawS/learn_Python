# Input ข้อความจาก User
try:
    fw=open("./Text/test.txt","a",encoding="UTF-8")
    while True:
        name=input("Ples input word :")
        if name == "0":
            break
        fw.writelines(name+"\n")
    fw.close()

except Exception:
    print("File not found.")