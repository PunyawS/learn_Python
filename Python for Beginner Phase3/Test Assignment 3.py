#Assignment โปรแกรม Crack รหัสผ่าน
import random

ATM_Password="1234"
result="" #เก็บผลลัพท์


while result!=ATM_Password:
    result =""
    for i in range(len(ATM_Password)):
        Passcode=random.choice("0123456789")
        result="".join(Passcode)+str(result)
        print(result)

print("CRACK PASSWORD IS :",result)