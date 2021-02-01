# Assignment 7 โปรแกรมแปลงอุณหภูมิ C ไป F
#https://www.youtube.com/watch?v=Lz-Q0kryP10&list=PLltVQYLz1BMBwqJysYnoEKWXUvqusJpgN&index=31
temp = input("Ples input :")
degree= int(temp[:-1]) #45
unit = temp[-1].upper() #C


if unit =="C":
    result =(9*degree)/5+32
    unit_re ="ฟาเรนไฮน์"
if unit =="F":
    result =(degree-32)*5/9
    unit_re ="เซลเซียส"


print("แปลงตัวเลข = ",degree,"เป็น",result, " = ",unit_re)