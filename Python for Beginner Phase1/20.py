#Assignment 4 
#แลกเงินและหาจำนวนแบงค์
#2000 => 1000 => 2 ใบ
#1500 => 1000 => 1 ใบ, 500 = 1 ใบ
#1800 => 1000 => 1 ใบ, 500 = 1 ใบ, 100 = 3 ใบ

money=int(input("Ples input your money :"))

#1500 => 1000 => 1 ใบ, 500 = 1 ใบ
if money>=1000:
    print("1000 บาท = ",money//1000,"ใบ")
    money = money%1000    #1500%1000 = 500

if money>=500:
    print("500 บาท = ",money//500,"ใบ")
    money%=500 #เขียนย่อ

if money>=100:
    print("100 บาท = ",money//100,"ใบ")
    money%=100

if money>=50:
    print("50 บาท = ",money//50,"ใบ")
    money%=50

if money>=20:
    print("20 บาท = ",money//20,"ใบ")
    money%=20