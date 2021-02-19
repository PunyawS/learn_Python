# ลบ Text ไฟล์
# import os เข้ามาทำงานเพื่อลบไฟล์
# os.remove("./Location file/name file.text")
import os
try:
    if os.path.exists("./text/111.txt"):
        os.remove("./text/111.txt")
        print("Complete")
    else:
        print("File not found. Check name again")

except Exception as e:
    print(e)