#Assignment 22
#จับคู่สินค้าและราคา

game=["PUBG","Season Pass Apex","Assassin's Creed","The sims 4"]
price=[300,399,899,1499]

for x,y in zip(game,price):
    print("Key :",x,"\t" ,"Price :",y)