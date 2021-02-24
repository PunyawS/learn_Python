name = input('Input your name :')
weight = float(input('Input your weight(kg) :'))
hight = float(input('Input your hight(cm) :'))/100
calculate = float(weight/(hight**2))
bmi = calculate

print(" Your name is :",name,"\n","Your hight is :",hight,' cm','\n',"Your weight is :",weight,'kg','\n',"Your BMI is :""%.2f" %bmi)