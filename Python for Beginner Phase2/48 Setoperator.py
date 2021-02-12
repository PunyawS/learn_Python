#Union
""" fruitA={"Banana","Apple","Lemon"}
fruitB={"Mango","Coconat","Watermelon"}
#allfurit=fruitA.union(fruitB)
fruitA.update(fruitB) #คล้ายกับ union
fruitC=fruitA.copy()
print(fruitA)
print(fruitC) """

#Difference
""" fruitA={"Banana","Apple","Lemon","Watermelon","Orange"}
fruitB={"Mango","Coconat","Watermelon","Orange"}
fruitC=fruitA.difference(fruitB)
print(fruitC) #fruitA - fruitB  """

#Intersection
""" fruitA={"Banana","Apple","Lemon","Watermelon","Orange"}
fruitB={"Mango","Coconat","Watermelon","Orange"}
fruitC=fruitA.intersection(fruitB)
print(fruitC) #fruitA - fruitB  """

#Superset&Subset
#Superset
fish={"ปลาฉลาม","ปลาทอง","ปลากัด","ปลาหางนกยุง","ปลาหมอ"}
#Subset
x={"ปลาทอง","ปลาหมอ","ปลากัด"}
print(fish.issuperset(x))
print(x.issubset(fish))