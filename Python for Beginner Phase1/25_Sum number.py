# Assignment 8
# Sum number
#1+2+3+4+5+6+7+8+9+10 = ?

i=1
summation = 0 #save summation number
average = 0 #sum/ i per round
round = int(input("Ples input round :"))

while i<=round:
    summation+=i #save summation i by 1 round
    i=i+1 #1+2+3+4+5+6+7+8+9+10 = ?
average = summation/round
print("Ans. summation :",summation)
print("Ave sum :", average)
