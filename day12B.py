file = open('input/input12.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

testinput = ['F10',
'N3',
'F7',
'R90',
'F11']

# input = testinput



boat_x = 0
boat_y = 0

way_x = 10
way_y = 1


def pusherbot(instruction):

    global way_x
    global way_y
    global boat_x
    global boat_y


    align = instruction[0]
    distance = int(instruction[1:])

    if align == 'N':
        way_y += distance
    if align == 'E':
        way_x += distance
    if align == 'S':
        way_y -= distance
    if align == 'W':
        way_x -= distance
    if align == 'F':
        boat_x += way_x*distance
        boat_y += way_y*distance

    if align == 'R':
        turn = int(distance/90)
        while turn > 0:

            temp_x = way_x
            temp_y = way_y
            if temp_y <= 0 and temp_x <= 0:
                way_x = temp_y
                way_y = abs(temp_x)
            if temp_y <= 0 and temp_x >= 0:
                way_y = -1 * temp_x
                way_x = temp_y

            if temp_y >= 0 and temp_x <= 0:
                way_y = abs(temp_x)
                way_x = temp_y

            if temp_y > 0 and temp_x > 0:
                way_y = -1 * temp_x
                way_x = temp_y
            turn -= 1


    if align == 'L':
        turn = int(distance / 90)
        while turn > 0:
            temp_x = way_x
            temp_y = way_y
            if temp_y <= 0 and temp_x <= 0:
                way_x = abs(temp_y)
                way_y = (temp_x)
            if temp_y <= 0 and temp_x >= 0:
                way_y = temp_x
                way_x = abs(temp_y)

            if temp_y >= 0 and temp_x <= 0:
                way_y = temp_x
                way_x = -1 * temp_y

            if temp_y >= 0 and temp_x >= 0:
                way_y = temp_x
                way_x = -1 * temp_y
            turn -= 1


for count, value in enumerate(input):
    pusherbot(value)

answer = abs(boat_x) + abs(boat_y)
print(str(answer))