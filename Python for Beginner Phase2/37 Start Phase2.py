#Primitive&Non-Primitive

#Primitive
""" a,b,c,d,e = 1,2,3,4,5 """

#Non-Primitive
number=[1,2,3,4,5] # sub set list is 1-10
""" #number=[] # List ว่าง
#name=["Piwpiw","Arpo"] # sub set list is piwpiw,arpo
#all=[10,"Piwpiw",True,1.11] """

#construtor
""" name=list([1,2,3,4,5,6,7,8,9,10]) # same name=["Piwpiw","Arpo"] """

#การเข้าถึงข้อมูลและแสดงผล
""" print(name)
print(all)
print(number[-1:])  """

#การแก้ไขข้อมูล
""" print("Before edit :",number)
number[2]=9
print("After edit :",number) """

#Loop
""" sum=0
for x in number:
    print("sub set :",x)
    sum+=x
print(sum) """

#การตรวจสอบข้อมูลสมาชิก
""" if 4 in number:
    print("เป็น")
else:
    print("ไม่เป็น") """

#การนับจำนวนสมาชิก
""" print(len(number)) """

names=["KKK","AAA","CCC"]
#Len ร่วมกับ Loop
""" for i in range(len(names)):
    print(names[i]) 
for kk in names:
    print(kk) """

#append, insert
""" print("Before :",names)
names.append("BBB") #ต่อท้าย
print("After :",names)
names.insert(1,"JJJ") #แทรกกลาง
print("After :",names) """

#remove,pop,del,clear
""" names.remove("AAA") #ตัวที่เลือก
print("Remove :",names) 
names.pop()         #ตัวท้ายสุด
print("Pop :",names)
del names[0]        #เลือกลบโดยบอก index
print(names)
names.clear()         #ลบสมาชิกออก
print("Clear :",names) """

#Copy data list A ==> B
""" x=[]
x=names.copy()
print(x) """

#รวมข้อมูลเพื่อทำ List ใหม่
meowmeow = ["Piwpiw","Arpo"]
""" allgroup=names+meowmeow
print(allgroup) """
#Extend รวมโดยใช้ List เดิม
""" meowmeow.extend(number)
print(meowmeow) """



#แสดงจำนวนสมาชิกที่ซ้ำกัน count
""" master=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7]
Y=master.count(4)
print(Y) """