#**kwargs

#*args
def add(*number):
    sum=0
    for i in number:
        sum+=i
    print(sum)

#**kwargs
def number(**kwargs):
    print(kwargs)

number(A="1",B="2",C="3")