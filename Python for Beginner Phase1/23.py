# String
# name="piwpiw" #"index" 

#print(name[-2])

#print(len(name)) #len function
#name=name.strip() # Delete spec left&right word or only left, only righy
#print(len(name))

#print(name.upper()) #change word to upper

#print(name.capitalize()) #chang first word to upper

#print(name.replace("piw","pun")) #input new word
""" x = "piw" in name
print(x) """   # check word in sentence => true, false

""" # จัด Format
fname = "punyawat"
lname = "suwannatat"
age = "24"
text = "Frist name :{}\tLast name :{}\tage :{}\tWork :{}"

print(text.format(fname,lname,age,"FA")) """

""" #นับจำนวนคำ
fruit = "Buy apple, banana, applepie at the market"
print(fruit.count("apple")) """

name="Mr.Punyawat Suwannatat"
#print(name.startswith("Mr."))
if name.startswith("Mr."):
    print("This is a man.")
else:
    print("Don't know")