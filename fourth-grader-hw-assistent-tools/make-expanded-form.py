#
# Make Expanded Form
#

from os import system

y = input("Enter a number to compare it to: ")

inpt = int(y)

def expanded_form(num):
    result = []
    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))
    return ' + '.join(result[::-1])

prnt = expanded_form(inpt)
print(prnt)