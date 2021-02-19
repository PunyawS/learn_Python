# Assignment
# Program Bank.

#data
account={"Mr.a":5000,"Mr.b":0}

def getbalance():
    print("Your money :",account)

def deposit(money):
    if not type(money) is int:
        raise Exception("กรุณาระบุตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("กรุณาระบุยอดใหม่อีกครั้ง")
    print("Deposit Mr.A :",money)
    account["Mr.a"]+=money

def withdrawn(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("กรุณาระบุตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("กรุณาระบุยอดใหม่อีกครั้ง")
    if money > account["Mr.a"]:
        raise Exception("ยอดเงินในบัญชีไม่เพียงพอ")
    
    print("Withdrawn Mr.A :",money)
    account["Mr.a"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("กรุณาระบุตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("กรุณาระบุยอดใหม่อีกครั้ง")
    if money > account["Mr.a"]:
        raise Exception("ยอดเงินในบัญชีไม่เพียงพอ")
   
    print("Transfer to Mr.B :",money)
    account["Mr.a"]-=money
    account["Mr.b"]+=money

try:
    getbalance()
    withdrawn(5000)
    getbalance()

except Exception as a:
    print(a)

finally:
    print("On process")


