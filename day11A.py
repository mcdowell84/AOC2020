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




# padding seating with '.'
for x in range(len(prev)):
    prev[x] = '.' + prev[x] + '.'

blankline = '.' * len(prev[0])
prev.insert(0, blankline)
prev.append(blankline)





def seating(line, prevline, nextline):

        newline = '.'
        for place in range(1, len(line)-1):  # check all chairs in line, without padding

            if line[place] == '.':
                newline = newline + '.'
            if line[place] != '.':          # look around seats

                area = []
                area.append(prevline[place - 1])     # NW
                area.append(prevline[place])         # NN
                area.append(prevline[place + 1])     # NE
                area.append(line[place + 1])    # EE
                area.append(nextline[place+1])     # SE
                area.append(nextline[place])       # SS
                area.append(nextline[place - 1])   # SW
                area.append(line[place - 1])    # WW

                counter = 0

                for o in range(len(area)):
                    if area[o] == '#':
                        counter += 1


                if line[place] == 'L':
                    if counter == 0:
                        newline = newline + '#'
                    if counter > 0:
                        newline = newline + 'L'

                if line[place] == '#':
                    if counter >= 4:
                        newline = newline + 'L'
                    if counter < 4:
                        newline = newline + '#'


        newline = newline + '.'  # re-add padding

        return newline





final = 0

while final < 1:
    temp = prev.copy()

    newstate = []
    for i in range(1, len(temp)-1):          # run over all lines in list

        line = temp[i]
        prevline = temp[i-1]
        nextline = temp[i+1]


        result = seating(line, prevline, nextline)
        newstate.append(result)

    blankline = '.' * len(newstate[0])  # re-add padding
    newstate.insert(0, blankline)
    newstate.append(blankline)


    if prev == newstate:
        final += 1
    else:
        prev = newstate

# print(final)
L_count = 0
for line in newstate:
    for chair in line:
        if chair == '#':
            L_count += 1

print(str(L_count))



