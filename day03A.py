# Day 3, part 1

input = open('input03.txt', 'r')
myList = input.readlines()
myList = [x.replace('\n', '') for x in myList]

steps = 0
treecounter = 0

for i in range(len(myList)):
    line = myList[i]
    if steps >= len(line) :
        steps = steps - len(line)
    if line[steps] == str('#'):
        treecounter += 1
    steps += 3

print(str(treecounter))