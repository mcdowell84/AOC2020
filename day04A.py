import re

input = open('input/input04.txt', 'r')
myFile = input.readlines()
batches = [x.replace('\n', '') for x in myFile]
passcount = 0

test_file = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
            'byr:1937 iyr:2017 cid:147 hgt:183cm',
            '',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
            'hcl:#cfa07d byr:1929',
            '',
            'hcl:#ae17e1 iyr:2013',
            'eyr:2024',
            'ecl:brn pid:760753108 byr:1931',
            'hgt:179cm',
            '',
            'hcl:#cfa07d eyr:2025 pid:166559648',
            'iyr:2011 ecl:brn hgt:59in']
test_file = batches
checklist = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

newlist = []
tempstring = ''
test_file.append(tempstring)

for i in range(len(test_file)):
    line = test_file[i]
    if len(line) > 0:
        tempstring = tempstring + test_file[i] + ' '
    if len(test_file[i]) == 0:
        newlist.append(tempstring)
        tempstring = ''


for x in range(len(newlist)):
    tempstring = ''
    line = newlist[x]
    for y in range(len(checklist)):
        if newlist[x].find(checklist[y]) != -1:
            tempstring = tempstring + str(1)
        if tempstring == '1111111':
            passcount += 1

print('Valid passports: ' + str(passcount))