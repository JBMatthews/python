# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

# CODE BELOW:
import re

fname = input("Enter file:")
if len(fname) < 1 :
    fname = "regex-sum-42.txt"
hand = open(fname)

for line in hand:
    strip = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    sints = float(stuff)
    print(type(sints))



# loop thru lines
#
# pull int from lines
#
# put in list, or dict
#
# convert to int
#
# add ints
#
# print answer
