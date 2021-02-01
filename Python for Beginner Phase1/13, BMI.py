# Assignment 1
# Cal BMI
# BMI = weight (kg) / Hight * Hight (m)

Weight = float(input("Ples input your weight (kg) = "))
Hight = float(input("Ples input your hight (cm) = "))/100
BMI = Weight/(Hight**2)

print("BMI =",BMI)
