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

byrRegex = re.compile(r'(byr:)(\d{4})')
iyrRegex = re.compile(r'(iyr:)(\d{4})')
eyrRegex = re.compile(r'(eyr:)(\d{4})')
hgtRegex = re.compile(r'(hgt:)(\d+)(in|cm)')
hclRegex = re.compile(r'(hcl:)#([a-f0-9]{6})')
eclRegex = re.compile(r'(ecl:)(amb|blu|brn|gry|grn|hzl|oth)')
pidRegex = re.compile(r'(pid:)(\d+)')

passcount = 0
tempstring = ''

for x in range(len(newlist)):
    text = str(newlist[x])
    tempstring = ''

    mo = byrRegex.search(text)
    if mo == None:
        byr = -1
    else:
        byr = int(mo.group(2))

    mo = iyrRegex.search(text)
    if mo == None:
        iyr = -1
    else:
        iyr = int(mo.group(2))

    mo = eyrRegex.search(text)
    if mo == None:
        eyr = -1
    else:
        eyr = int(mo.group(2))

    mo = hgtRegex.search(text)
    if mo == None:
        hgt = -1
    else:
        hgt = int(mo.group(2))

    mo = hgtRegex.search(text)
    if mo == None:
        hgt_unit = 'none'
    else:
        hgt_unit = str(mo.group(3))

    mo = hclRegex.search(text)
    if mo == None:
        hcl = 'none'
    else:
        hcl = str(mo.group(2))

    mo = eclRegex.search(text)
    if mo == None:
        ecl = 'none'
    else:
        ecl = str(mo.group(2))

    mo = pidRegex.search(text)
    if mo == None:
        pid = 'none'
    else:
        pid = str(mo.group(2))

    if 1920 <= byr and 2002 >= byr:
        tempstring = tempstring + str(1)
    if iyr >= 2010 and iyr <= 2020:
        tempstring = tempstring + str(2)
    if eyr >= 2020 and eyr <= 2030:
        tempstring = tempstring + str(3)
    if hgt_unit == 'none':
        pass
    else:
        if hgt_unit == 'cm':
            if hgt >= 150 and hgt <= 193:
                tempstring = tempstring + str(4)
        if hgt_unit == 'in':
            if hgt >= 59 and hgt <= 76:
                tempstring = tempstring + str(5)
    if hcl != 'none':
        tempstring = tempstring + str(6)
    if ecl != 'none':
        tempstring = tempstring + str(7)
    if len(pid) == 9:
        tempstring = tempstring + str(8)

    if len(tempstring) == 7:
        passcount += 1
        tempstring = ''

print(str(passcount))