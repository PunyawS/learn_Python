x=input("Ples input order:")
market={
    "Starbuck":{
        "name":"A",
        "menu":["coffee","milk","green tea","tea"],
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
if x in market["Starbuck"]["menu"]:
    print("Your order is :", x, market["Starbuck"]["zone"])
    if x in market["KFC"]["menu"]:
        print(market["KFC"]["menu"])
    if x in market["McDonald's"]["menu"]:
        print(market["McDonald's"]["menu"])
    if x in market["Pizza Hut"]["menu"]:
        print(market["Pizza Hut"]["menu"])
else:
    print("Sorry. We don't have order.")