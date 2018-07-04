# 10.2 Assignment - testing playground
#
# Input File:
# mbox-short.txt
#
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#
# GO ON AN TEST BELOW:


# *** Imagine this as an array after you split it

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#[  0,        1                   , 3, 4 , 5,   6    ,  7]
# File Input Section Process
fname = input("Enter file:")
if len(fname) < 1 :
    fname = "mbox-short.txt"
hand = open(fname)

# Intializing an Empty Dictionary
di = dict()

# Adding Input Section to Dictionary (di)
#
# For Each Line in Input Section
for lin in hand:
    # If It Does NOT Startwith, Continue
    if not lin.startswith("From "):
        continue
    # Catcher
    #x = lin.find(":")   # ** This starts the index where the colin is, or right after 09 in '09:14:16'
    #y = lin.find(' ',x)     # ** This would find a space in 'x' if that's what you were doing. remember, the find() function returns an index, not a string.probably errors here.
    # if it didn't error, and you inputed the string before the colon it would still find the first space
    # which is after 'From ' and return that index.

    #data = lin[x : y]   # ** This if going from the above code would return everything after the first colon and loop around i think to the first space. weird outcome i think.not sure
    # ----------- My thoughts here
    # we already have the line. let's do this:
    # 1. ) split it into an array,
    # 2.) then get the item with time,
    # 3.) split on colon- should give you 3 items, first item is the hour

    line_words = lin.split()   # split into an array
    print(line_words)
    time = line_words[5]       # get the time item
    time_data = time.split(':')  # ** split the time by colon. so '09:14:16' becomes an array => [09,14,16]
    hour = time_data[0]     # get the hour

    # ---------


    #lin = lin.rstrip()
    #wds = data.split()
    di[hour] = di.get(hour, 0) + 1  # count number of occurences for hour
    # ** What this idiom is doing is saying: hey, get the value for 'hour' if it's not in the dictionary
    # ** then return the default value we supply,which is 0, then add 1.
    # The first loop around no value is in the dictionary so it will return 0+1 = 1, for our first occurenct.
    # so if di[hour] is hour '09', the first time will store 1. so di[09] = 1. The next time it will
    # get the key and add 1. So it will get the key '09' which is 1, then add 1 to it. and so on for each occurance

print(di)
    # you don't have to interate th
#
#
# tmp = list()
# for k,v in di.items() :
#     newt = (v,k)
#     tmp.append(newt)
#
# tmp = sorted(tmp, reverse=True)
# print('Sorted', tmp[2 :5])
# for v,k in tmp[:5] :
#     print(k,v)



find index of index
index -2
