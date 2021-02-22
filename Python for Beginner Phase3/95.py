#Random Utility
import random

x=random.random() #random 0.0 - 1.0
print(x)

for i in range(10): #random 0.0 - 1.0, 10 times
  x=random.random()
  print(x)

for i in range(15):
    x=random.uniform(5,10) # random 5 - 10, 15 times
    print(x)

for i in range(15):
    x=random.randrange(1,10,2) #random 1-9, 1+2=3, 3+2=5, 5+2=7, 7+2=9
    print(x)

for i in range(15):
    x=random.randint(1,5) #random 1 - 5
    print(x)

#สุ่มค่าใน List
x=[1,2,3,4,5,6,7,"A","B","C"]
for i in range(10):
    y=random.choice(x)
    print(y)

x=[1,2,3,4,5,6,7,"A","B","C"]
for i in range(10):
    random.shuffle(x)
    print(x)    
    