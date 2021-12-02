import re

input = ['nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6']

file = open('input/input08.txt', 'r')
myFile = file.readlines()
myFile = [x.replace('\n', '') for x in myFile]
input = myFile

prog = re.compile(r'([a-z]{3})\s[+|-](\d+)')  # matches 3 letter word +/-number

length = len(input)
# length = 3

for x in range(length):
        accumulator = 0
        newinput = input.copy()
        line = newinput[x]
        splitter = prog.search(line)
        instruct = splitter.group(1)
        if instruct == 'nop':
                line = line.replace('nop', 'jmp')
        if instruct == 'jmp':
                line = line.replace('jmp', 'nop')

        if newinput[x] != line:
                newinput[x] = line

        i = 0
        end = len(newinput) - 1

        while i <= end:
                if i == end:
                        print('end of program reached, acc = ' + str(accumulator))

                        break
                line2 = newinput[i]

                splitter = prog.search(line2)
                instruct = splitter.group(1)
                number = 1
                number = int(line2[4] + str(1)) * int(splitter.group(2))
                # print('splittergroep=' + splitter.group(2))
                # print('number=' + str(number))
                n = 0

                if instruct == 'stp':

                        break


                if instruct == 'nop':
                        pass
                if instruct == 'jmp':
                        n = number -1
                if instruct == 'acc':
                        accumulator += number

                newinput[i] = 'stp +666'

                i = i + 1 + n