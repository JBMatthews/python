# USER INPUT

pick = input("Type PERIMETER or AREA? ")
upcase = pick.upper()
print("You've choosen: " + upcase)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# LOOP LOGIC
if upcase == "PERIMETER":
    # -- CALC PERIMETER
    result = num1 + num2 + num1 + num2
    print("The perimeter is: " + str(result))
elif upcase == "AREA":
    # -- CALC SQ. FEET
    result = num1 * num2
    print("The area is: " + str(result))
else:
    print("Try Again! ...probably just spelling error. ")
