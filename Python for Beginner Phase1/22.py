# Cal BMI
# BMI = weight (kg) / Hight * Hight (m)
# input / convert to integer
""" 
< 18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วนระดับที่ 1
>30.0 = โรคอ้วนระดับอันตราย
"""

weight=float(input("Ples input your weight (kg) :"))
hight=float(input("Ples input your hight (cm) :"))/100
BMI = float(weight/(hight**2))
#print("Your BMI is =""%.2f" % BMI)

result="Don't know state"
if BMI>=0:
    if BMI<=18.0:
        result="ต่ำกว่าเกณฑ์"
    
    elif BMI>=18.5 and BMI<=22.9:
        result="สมส่วน"
    
    elif BMI>=23.0 and BMI<=24.9:
        result="น้ำหนักเกิน"
    
    elif BMI>=25.0 and BMI<=29.9:
        result="โรคอ้วนระดับที่ 1"
        
    else:
        result="โรคอ้วนระดับอันตราย"

#print("Your BMI State is = ",result)
print("Your BMI is =""%.2f" % BMI,"\n","Your BMI State is = ", result)
print("End process")