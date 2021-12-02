# Day 3, part 2

input = open('input03.txt', 'r')
myList = input.readlines()
myList = [x.replace('\n', '') for x in myList]

multiplier = 1

# x along, 1 down
for x in [1,3,5,7]:
    steps = 0
    treecounter = 0
    for i in range(len(myList)):
        line = myList[i]
        if steps >= len(line) :
            steps = steps - len(line)
        if line[steps] == str('#'):
            treecounter += 1
        steps += x
    multiplier = multiplier * treecounter



# 1 along, 2 down

steps = 0
treecounter = 0

for y in range(len(myList)):
    line = myList[y]
    if steps == len(line):
        steps = 0
    if y % 2 == 0:
        if line[steps] == str('#'):
            treecounter += 1
        steps += 1

multiplier = multiplier * treecounter
print('Multiplier: ' + str(multiplier))