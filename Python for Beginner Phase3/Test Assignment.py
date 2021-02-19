
account={"A":5000,"B":0}

def bal():
    print("Your money :",account)

def deposit(money):
    if not type(money) is int:
        raise Exception
    if money <= 0:
        raise Exception
    print("Deposit money :",money)
    account["A"]+=money

def withdrawn(money):
    if not type(money) is int:
        raise Exception
    if money <= 0:
        raise Exception
    if money > account["A"]:
        raise Exception ("Over Bal. Ples Try again.")
    
    print("withdrawn money :",money)
    account["A"]-=money


try:
    x=int(input("Ples input your deposit money :"))
    deposit(x)
    bal()
    y=int(input("Ples input your withdrawn money :"))
    withdrawn(y)
    bal()
except Exception as a:
    print(a)