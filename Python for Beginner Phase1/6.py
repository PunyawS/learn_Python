#Type Coversion
x = 10
y = 3.14
z = "20"

result = x+y


print(type(x))
print(type(y))
print(type(z))
print(result,'\n')

# str => int
print(int(z))
resultstrtoint = x+int(z)
print(resultstrtoint,'\n')

# int => str
print(str(x))
resultinttostr = z+str(x)
print(resultinttostr,'\n')

# str => float
print(float(z))
resultstrtofloat = y+float(z)
print(resultstrtofloat,'\n')

# float => int
print(y)
resultfloattoint = int(y)
print(resultfloattoint,'\n')

z = float(z)
z = z+50
print(z)