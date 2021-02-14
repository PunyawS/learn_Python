#*args

def number(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

number(10,20)