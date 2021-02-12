#List , Tuple ต้องจำ Index หากต้องการใช้งานข้อมูล
""" x=list(["a"])
y=tuple(("b"))
print(type(x))
print(type(y))
 """
#Dictionary
#Dictionary => key(Index), value(value in index)

# dict กำหนดชื่อ key ของ index ได้
color={"blue":"สีน้ำเงิน","yellow":"สีเหลือง"} #{key:value}
colors=dict({"blue":"สีน้ำเงิน","yellow":"สีเหลือง"})
""" print(type(color))
print(type(colors))
print(color["blue"])
print(colors["yellow"]) """

#Edit
""" color["blue"]="น้ำเงิน" """
#Add
color.update({"green":"สีเขียว","orange":"สีส้ม"})
""" print(color) """

#for loop
""" for x,y in color.items():
    print(x,y)
 """
#การลบข้อมูลสมาชิกโดยใช้ pop
""" color.pop("blue")
color.popitem()
color.clear()
del color()
print(color) """

#copy
""" x=color.copy()
print(x) """

#Dict in dict
market={
    "Starbuck":{
        "name":"A",
        "menu":["coffee","milk","green tea"],
        "zone":"1"
    },
    "KFC":{
        "name":"B",
        "menu":["Chicken"],
        "zone":"2"
    },
    "McDonald's":{
        "name":"C",
        "menu":["Burger","Chicken"],
        "zone":"3"
    },
    "Pizza Hut":{
        "name":"D",
        "menu":["Pizza"],
        "zone":"4"
    }
}
""" 
if x in market["Starbuck"]["menu"]:
    print("Yes")
else:
    print("We don't have.")
 """
print(market["KFC"]["menu"])