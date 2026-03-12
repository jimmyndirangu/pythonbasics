# A script that checks if someone is eligible to vote
age=int(input("Enter age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote. Underage....")

# A script that checks if a number is odd or even
num=int(input("Enter a number that is even:"))
if num %2==0:
    print("Correct")
else:
    print("Wrong")
   
# A script that checks ("python123") is valid
# else wrong password
password=input("Enter password:")
if password == "python123":
    print("Correct password")
else:
    print("Wrong password")

# a script that checks the largest number among three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
elif num3>num1 and num3>num2:
    print(f"{num3} is the largest number")
else:
    print("All the numbers are equal")
