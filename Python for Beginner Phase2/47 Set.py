#สร้างแบบปกตื
x={"ABC","CBA"}
print(x)

#constructor
a=set(("ABC","CBA"))
print(type(a))

#เพิ่มข้อมูลสมาชิกทีละตัว
a.add("XYZ")
a.add("ZYX")

#เพิ่มข้อมูลสมาชิกทีละหลายๆตัว
lis=["A","B","C"]
a.update(lis)
print(a)

#for loop ในการดึงข้อมูล
for y in a:
    print("ข้อมูล :", y)

#แสดงจำนวนสมาชิกใน Set
print(len(a))

#ตรวจสมาชิกข้อมูลใน Set
if "A" in a:
    print("OK")
else:
    print("No")

#การลบข้อมูล
a.remove("A")
print(a)