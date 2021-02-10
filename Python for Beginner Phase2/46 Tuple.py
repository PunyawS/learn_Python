""" x=(1,2,3,4,5) #tuple
y=[1,2,3,4,5] #list
z=list(x) """

""" #print(x)
#print(y)
z[0]=7 #tuple to list
x=tuple(z) #list to tuple
print(z)
print(x) """

""" for i in x:
    print(i) """

""" if 7 in x:
    print("OK")
else:
    print("No") """

#print(len(x))

""" for i in range(len(x)):
    print(x[i]) """

""" a=("as","bd")
b=tuple(("a","b"))
c="ABB"
name=a+(c,)
print(name)
 """

""" a=(1,2,3,4,"LL")
b=list(a)
b[4]=5
a=tuple(b)
print(a) """

""" a=(1,2,3,4,"LL")
b=list(a)
b.remove("LL")
a=tuple(b)
print(a) """

""" a=(1,1,1,1,2,1,4,15)
b=a.count(1)
c=a.index(1)
print(b)
print(c) """

""" x=(1,4,3,5,8,0)
y=list(x)
y.sort()
x=tuple(y)
print(x) """

#จับคู่
""" x=(10,20,30)
a,b,c=x
print(a,b,c,) """

#สลับ Tuple
""" x=(10,20)
y=(30,40)
x,y=y,x
print("x :",x,"y :",y) """

#tuple => string
""" cha=('p','u','n')
name="".join(cha)
print(name) """

#เรียงข้อมูลจากหลังมาด้านหน้า
x=(1,2,5,7,10,4)
y=reversed(x)
print(tuple(y))