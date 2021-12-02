test_file =['abc',
            '',
            'a',
            'b',
            'c',
            '',
            'ab',
            'ac',
            '',
            'a',
            'a',
            'a',
            'a',
            '',
            'b',]

input = open('input/input06.txt', 'r')
myFile = input.readlines()
myFile = [x.replace('\n', '') for x in myFile]
test_file = myFile

abc = 'abcdefghijklmnopqrstuvwxyz'
counter = 0
test_file.append('')
tempstring = ''
newlist = []

for foo in range(len(test_file)):
    line = test_file[foo]
    if len(line)>0:
        tempstring = tempstring + '0' + line
    if len(test_file[foo]) == 0:
        newlist.append(tempstring)
        tempstring = ''

for i in range(len(newlist)):

    line = newlist[i]
    for x in range(len(abc)):
        if line.count(str(abc[x])) != 0 and line.count(str(abc[x])) == line.count(str('0')):
            counter += 1

print(str(counter))