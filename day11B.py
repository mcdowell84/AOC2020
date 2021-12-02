from copy import copy, deepcopy


file = open('input/input11.txt', 'r')
prev = file.readlines()
prev = [x.replace('\n', '') for x in prev]

test_init = ['L.LL.LL.LL',
        'LLLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLLL',
        'L.LLLLLL.L',
        'L.LLLLL.LL']

# prev = test_init


m1 = []     # create matrix
for count, value in enumerate(prev):
    newlist = list(value)
    m1.append(newlist)


def chairwalker(y,x):
    chcount = 0
    for diry in [-1, 0, 1]:
        for dirx in [-1, 0, 1]:
            if diry == 0 and dirx == 0:
                continue

            step = 0
            skip = 0

            while skip < 1:
                step += 1
                checky = diry * step  # y location
                checky = y + checky
                checkx = dirx * step    # x location
                checkx = x + checkx

                if checky < 0 or checky >= len(m1):
                    skip = 1
                    continue

                if checkx < 0 or checkx >= len(m1[0]):
                    skip = 1
                    continue

                check = temp[checky][checkx]

                if check == '#':
                    chcount += 1
                    skip = 1
                    continue

                if check == '.':
                    continue

                if check == 'L':
                    skip = 1
                    continue

    return chcount

go = 1

while go == 1:
    temp = deepcopy(m1)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            count = chairwalker(i,j)

            if temp[i][j] == 'L' and count == 0:
                m1[i][j] = '#'

            if temp[i][j] == '#' and count >= 5:
                m1[i][j] = 'L'
    if temp == m1:
        go = 0

final_count = 0
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if m1[i][j] == '#':
            final_count += 1

print(str(final_count))