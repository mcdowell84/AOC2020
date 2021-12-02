import re

input01 = open('input02.txt', 'r')
myList = input01.readlines()
passlist = [x.replace('\n', '') for x in myList]

rightpass = 0

numRegex = re.compile(r'(\d\d|\d)-(\d\d|\d)')
letRegex = re.compile(r'(\w):')
passRegex = re.compile(r': (\w+)')

for x in range(len(passlist)):
    text = str(passlist[x])

    mo = numRegex.search(text)
    mo2 = letRegex.search(text)
    mo3 = passRegex.search(text)

    letter = str(mo2.group(1))
    password = str(mo3.group(1))
    low = int(mo.group(1))
    high = int(mo.group(2))

    count = 0

    for i in password:
        if i == letter:
            count = count + 1
    if low <= count and high >= count:
        rightpass += 1


print('Counter: ' + str(rightpass))
