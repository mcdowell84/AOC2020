input = open('input/input05.txt', 'r')
myFile = input.readlines()
batches = [x.replace('\n', '') for x in myFile]
winner = 0


for x in range(len(batches)):
    min = 0
    max = 127
    bereik = max - min + 1
    chairmin = 0
    chairmax = 7
    chairbereik = chairmax - chairmin + 1
    teststring = batches[x]
    for i in range(len(teststring)):
        letter = teststring[i]
        if i <= 6:
            if letter == 'F':
                max = max - (0.5*bereik)
                bereik = max - min + 1
            if letter == 'B':
                min = min + (0.5*bereik)
                bereik = max - min + 1
        if i > 6:
            if letter == 'R':
                chairmin = chairmin + (0.5 * chairbereik)
                chairbereik = chairmax - chairmin + 1
            if letter == 'L':
                chairmax = chairmax - (0.5 * chairbereik)
                chairbereik = chairmax - chairmin + 1
    seatid = min*8+chairmin
    if seatid > winner:
        winner = seatid
print(str(winner))