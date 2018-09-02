import turtle
from os import system

system('say something')

xsay = input("Enter first number: ")
ysay = input("Enter second number, now: ")

num1 = int(xsay)
num2 = int(ysay)


# CALC SQ. FEET
result = num1 * num2
system('say ' + str(result))

# CALC PERIMETER
result = num1 + num2 + num1 + num2
system('say ' + str(result))

# TURTLE DRAWING
turtle.shape("turtle")
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.exitonclick()
