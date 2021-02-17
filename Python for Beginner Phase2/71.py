#Assignment 29
#ฟังก์ชั่นค้นหาเบอร์โทรศัพท์

data={
    "191":"แจ้งเหตุด่วน",
    "1669":"เรียกรถโรงพยาบาล",
    "1447":"ดับเพลิง",
    "1150":"หิวข้าว"
}

def searchnumber(message):
    for key,value in data.items():
        if value==message:
            print("เบอร์",key)
        elif key==message:
            print("=",value)
        else:
            print("ไม่มีรายการนี้")
            return

x=input("Ples input number or word :")
searchnumber(x)