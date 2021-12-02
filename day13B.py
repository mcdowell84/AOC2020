import re

file = open('input/input13.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

testinput = ['939',
    '7,13,x,x,59,x,31,19']

testinput = ['939',
    '3,5,7']

input = testinput

buses = input[1].split(",")


for count, value in enumerate(buses):
    if value != 'x':
        buses[count] = int(value)

answers = []

def timerbot(timestamp):
    global answers
    for count, value in enumerate(buses):
        if value != 'x':
            if (timestamp + count) % value != 0:
                return False
    answers.append(timestamp)
    return 1


# timestamp = 7
timestamp = 0
answer = 0

while answer < 20:

    answer += timerbot(timestamp)
    timestamp += 1

print(answers)