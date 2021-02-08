#Assignment 22.1
#จับคู่คำทักทายของบุคคล

saysomething=["Hi","Hello"]
people=["A","B"]
conversation=[]
""" for x in saysomething:
    for y in people:
        conversation.append(x+y) """
conversation=[x+y for x in saysomething for y in people]
print(conversation)


""" for x,y in zip(saysomething,people):
    print(y,":",x) """