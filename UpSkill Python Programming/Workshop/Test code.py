print('a','b','c','d', sep = '# ')
print('Hello world'.title())

mylist = [1,3,5,2,4,6] 
mylist.insert(0,0) #0 1 3 5 2 4 6
print(mylist)
mylist[0:3] = [0,1,2] #0 1 2 5 2 4 6
print(mylist)
mylist.pop(4) # 0 1 2 5 4 6
print(mylist)

print('asdsadA'.upper())