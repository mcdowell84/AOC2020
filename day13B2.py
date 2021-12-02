import re

file = open('input/input13.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

testinput = ['939',
    '7,13,x,x,59,x,31,19']

testinput = ['939',
    '7,13,x,x,59']

input = testinput

# 7x = 13y -1 = 59z - 4

buses = input[1].split(",")

offset = []


for count, value in enumerate(buses):
    if value != 'x':
        buses[count] = int(value)






answers = []

def timerbot(timestamp):
    global answers
    for count, value in enumerate(buses):
        busid = value
        off = count
        if (timestamp+off) % busid != 0:
            return False
    answers.append(timestamp)
    return 1


timestamp = 0
# timestamp = 100000000000000 - (100000000000000%buslist[0])
answer = 0

while answer < 10:

    answer += timerbot(timestamp)
    timestamp += 1

print(answers)

