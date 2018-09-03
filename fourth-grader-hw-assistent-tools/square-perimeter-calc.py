from os import system

# USER INPUT
pick = input("PERIMETER or AREA?")
print("You've choosen: " + pick)

xsay = input("Enter your first number: ")
ysay = input("Enter your second number: ")



num1 = int(xsay)
num2 = int(ysay)

# LOOP LOGIC
if pick == "O":
    # -- CALC PERIMETER
    result = num1 + num2 + num1 + num2
    print(result)
    # system('say ' + str(result)

else:
    # -- CALC SQ. FEET
    result = num1 * num2
    print(result)
    # system('say ' + str(result)
