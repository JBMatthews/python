# Compare Numbers
from os import system

x = input("Enter your first number: ")
y = input("Enter a number to compare it to: ")

num1 = int(x)
num2 = int(y)

print("The numbers you entered were: " + str(num1) + " and " + str(num2))

# IF/ELSE LOOP
if num1 > num2:
    answr = num1
    print(x + " is greater than " + y)
elif num1 < num2:
    answr = num2
    print(x + " is less than " + y)
elif num1 == num2:
    answr = ""
    print("Both numbers are equal")
else:
    print("ERROR: Try Again")

# SAY FUNCTION
def say():
    if answr is num1:
        system("say " + x + " is greater than " + y)
    elif answr is num2:
        system("say " + x + " is less than " + y)
    else:
        system("say Both numbers are equal")

say()
