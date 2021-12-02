import re

testfile = [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.']

input = open('input/input07.txt', 'r')
myFile = input.readlines()
myFile = [x.replace('\n', '') for x in myFile]
testfile = myFile

bagcounter = 0
tempcounter = 0


prog = re.compile(r'(?<=\d\s)[a-z]+\s[a-z]+(?=\sbag)')  # matches '[word word]' when preceded by '[number][space]' and followed by ' bag'
indexlist = []
for w in range(len(testfile)):
        line = testfile[w]
        mainbag = re.match(r'([a-z]+\s[a-z]+) bags contain', line)  # matches first bag of line
        mainbag = mainbag.group(1)
        indexlist.append(mainbag)

#print(len(fillerbags))

def bagcheck(bagindex):
        global tempcounter
        # global lister
        line = testfile[bagindex]
        # print('>Bag to check: ' + 'L' + str(bagindex) + ' G' + str(lister) + ' - ' + line)

        fillerbags = prog.findall(line)
        if len(fillerbags)==0:
                # print('>>>Contains no bags')
                pass
        if len(fillerbags)>0:
                for y in range(len(fillerbags)):
                        if fillerbags[y] == 'shiny gold':
                                tempcounter += 1
                                # print('Gotcha: ' + line)
                                # print('Bag counter: ' + str(tempcounter))
                                # bagindex = lister
                                return


                        else:

                                newindex = indexlist.index(fillerbags[y])
                                bagcheck(newindex)

for q in range(len(testfile)):
        # lister = q
        bagcheck(q)
        if tempcounter > 0:
                bagcounter += 1
        tempcounter = 0

print(str(bagcounter))