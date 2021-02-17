#lambda function
# Function ไม่ระบุชื่อ
""" 
lambda arguments : expression
"""

""" x=lambda name:name
y=lambda x,y: x+y

print(x("Piw"))
print(y(10,20)) """

def pow(x):
    return lambda a:x**a

y=pow(5)    #y is lambda a:5**a
result=y(2) #result = 5**2
print(result)