# เขียน Text ไฟล์ต่อจากไฟล์เดิม

try:
    fr=open("./Text/test.txt","r",encoding="UTF-8")
    s=fr.readlines()
    for i in s:
        print("=>",i)

    fw=open("./Text/test.txt","a",encoding="UTF-8")
    s=fw.writelines("\nHi.")

    fr.close()
    fw.close()

except Exception:
    print("File not found.")