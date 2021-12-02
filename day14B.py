import re

file = open('input/input14.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

mask = ''

progmem = re.compile(r'(?<=\[)[0-9]+(?=\])')  # matches '[numbers]'
progval = re.compile(r'(?<=\]\s=\s)[0-9]+')  #  matches '] = numbers'


length = 0

for count, value in enumerate(input):
    start = value[:3]
    if start == 'mem':
        mem = progmem.search(value)
        mem = int(mem.group())
        if mem > length:
            length = mem

output = [0] * (length)


def robot(input):
    global mask
    global output
    global address
    start = input[:3]
    if start == 'mem':
        mem = progmem.search(input)
        mem = int(mem.group())

        val = progval.search(input)
        val = int(val.group())
        val = format(val, '036b')

        new = list(mask)

        for count, value in enumerate(new):
            if value == 'X':
                pass
            if value == '0':
                new[count] = val[count]
            if value == '1':
                pass
        result = ''.join(new)

        output[mem-1] = result

def linereader(input):
    temp = ''
    for i in input:
        if i == '0':
            temp = temp + '0'
        if i == '1':
            temp = temp + '1'
        if i == 'X':
            for x in [0,1]:



    if start == 'mas':
        mask = input[-36:]


for count, value in enumerate(input):
    robot(value)

for count, value in enumerate(output):
    linereader(value)

answer = sum(output)
print(str(answer))
