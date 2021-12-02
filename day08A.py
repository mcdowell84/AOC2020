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

accumulator = 0

i = 0
end = len(input)-1




while i < end:
        line = input[i]
        splitter = prog.search(line)
        instruct = splitter.group(1)
        number = int(line[4] + str(1)) * int(splitter.group(2))
        n = 0

        if instruct == 'stp':
                print('Stop the clock!')
                print('acc: ' + str(accumulator))
                break
        if instruct == 'nop':
                pass
        if instruct == 'jmp':
                n = number -1
        if instruct == 'acc':
                accumulator += number

        input[i] = 'stp +666'
        i += 1 + n
        if i == len(input)-1:
                print('End of program reached!')
                print('acc: ' + str(accumulator))
                break
