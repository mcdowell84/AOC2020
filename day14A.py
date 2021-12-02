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
                new[count] = val[count]
        result = ''.join(new)
        result = int(result, 2)
        output[mem-1] = result




    if start == 'mas':
        mask = input[-36:]


for count, value in enumerate(input):
    robot(value)

answer = sum(output)
print(str(answer))
