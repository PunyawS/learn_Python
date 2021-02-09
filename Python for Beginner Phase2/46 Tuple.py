x=(1,2,3,4,5) #tuple
y=[1,2,3,4,5] #list
z=list(x)

#print(x)
#print(y)
z[0]=7 #tuple to list
x=tuple(z) #list to tuple
print(z)
print(x)