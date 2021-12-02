import re
import math

testfile = [
        'shiny gold bags contain 2 dark red bags.',
        'dark red bags contain 2 dark orange bags.',
        'dark orange bags contain 2 dark yellow bags.',
        'dark yellow bags contain 2 dark green bags.',
        'dark green bags contain 2 dark blue bags.',
        'dark blue bags contain 2 dark violet bags.',
        'dark violet bags contain no other bags.']

input = open('input/input07.txt', 'r')
myFile = input.readlines()
myFile = [x.replace('\n', '') for x in myFile]
testfile = myFile

bagcounter = 0

prog = re.compile(r'\d\s[a-z]+\s[a-z]+(?=\sbag)')  # matches '[number] [word word]' when followed by ' bag'
prog2 = re.compile(r'(\d)\s([a-z]+\s[a-z]+)')  # matches '[number] [word word]'

indexlist = []

for w in range(len(testfile)):
        line = testfile[w]
        mainbag = re.match(r'([a-z]+\s[a-z]+) bags contain', line)  # matches first bag of line
        mainbag = mainbag.group(1)
        indexlist.append(mainbag)

start = indexlist.index('shiny gold')
multiplier = 1
multipliers = []
multipliers.append(1)
number = 1

def bagcheck(bagindex):
        global bagcounter
        global multipliers
        multiplier = math.prod(multipliers)
        global number

        line = testfile[bagindex]
        fillerbags = prog.findall(line)

        if len(fillerbags)==0:
                pass
        if len(fillerbags)>0:
                for y in range(len(fillerbags)):
                        bagtocheck = fillerbags[y]

                        bagsplitter = prog2.search(bagtocheck)
                        number = int(bagsplitter.group(1))
                        bag = bagsplitter.group(2)
                        multiplier = math.prod(multipliers)
                        bagcounter = bagcounter + number * multiplier
                        multipliers.append(number)



                        newindex = indexlist.index(bag)
                        bagcheck(newindex)
                        multipliers.pop()


bagcheck(start)
print(str(bagcounter))