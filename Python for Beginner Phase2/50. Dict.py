#List , Tuple ต้องจำ Index หากต้องการใช้งานข้อมูล
""" x=list(["a"])
y=tuple(("b"))
print(type(x))
print(type(y))
 """
#Dictionary
#Dictionary => key(Index), value(value in index)

# dict กำหนดชื่อ key ของ index ได้
color={"blue":"สีน้ำเงิน","yello":"สีเหลือง"} #{key:value}
colors=dict({"blue":"สีน้ำเงิน","yello":"สีเหลือง"})
print(type(color))
print(type(colors))
print(color["blue"])
print(colors["yello"])