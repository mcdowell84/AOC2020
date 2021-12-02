import re

file = open('input/input13.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

testinput = ['939',
    '7,13,x,x,59,x,31,19']

# input = testinput

time = int(input[0])
lowest = 1000000
busid = 0
buses = re.findall('[0-9]+', input[1])
for i in range(0, len(buses)):
    buses[i] = int(buses[i])

def timerbot(bustime):
    global time
    global lowest
    global busid

    time1 = time % bustime
    wait = bustime - time1
    if wait < lowest:
        lowest = wait
        busid = bustime


for count, value in enumerate(buses):
    timerbot(value)

print(str(busid*lowest))