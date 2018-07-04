count = dict()

count['csev'] = 0
count['cwen'] = 0

print(count)

i = 0

while i < 10:
    count['csev'] = count['csev'] + 1
    i = i + 1

print(count.items())
