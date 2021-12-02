file = open('input/input12.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

testinput = ['F10',
'N3',
'F7',
'R90',
'F11']

# input = testinput

# 0 = N, 1=E, 2=S, 3=W, 4=N etc
dir = 1
locx = 0
locy = 0

def pusherbot(instruction):
    global dir
    global locx
    global locy

    align = instruction[0]
    distance = int(instruction[1:])
    if align == 'N':
        locy += distance
    if align == 'E':
        locx += distance
    if align == 'S':
        locy -= distance
    if align == 'W':
        locx -= distance
    if align == 'F':
        if dir%4 == 0:
            locy += distance
        if dir%4 == 1:
            locx += distance
        if dir%4 == 2:
            locy -= distance
        if dir%4 == 3:
            locx -= distance
    if align == 'R':
        turn = int(distance/90)
        dir += turn
    if align == 'L':
        turn = int(distance/90)
        dir -= turn



for count, value in enumerate(input):
    pusherbot(value)

answer = abs(locx) + abs(locy)
print(str(answer))