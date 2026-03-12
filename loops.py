num=5
while num<=15:
 print(num)
 num+=1

# create a script starting with 50
num2=50
while num2>=0:
 print(num2)
 num2-=5


secret=7
guess=0

while guess!=secret:
  guess=int(input("Enter number:"))
  if guess==secret:
   print("Correct")
  else:
   print("Try again")

cars=["Mercedes","BMW","Audi","RollsRoyce","Subaru"]
for i in cars:
 print(i)

