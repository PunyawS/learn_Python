#Assignment โปรแกรม Crack รหัสผ่าน
import random

ATM_Password="19k"
result="" #เก็บผลลัพท์

while result!=ATM_Password:
    result =""
    for i in range(len(ATM_Password)):
        Passcode=random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
        result="".join(Passcode)+str(result)
        print(result)

print("CRACK PASSWORD IS :",result)