# recursive function
# if len[fillerbags]==0 then stop function, go onto next bag
# if fillerbag is shiny gold bag then add mainbag to list
# if fillerbag contains other bags then check those fillerbags

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

bagcounter = 0
#mainbag = re.match(r'([a-z]+\s[a-z]+) bags contain', line)  # matches first bag of line
prog = re.compile(r'(?<=\d\s)[a-z]+\s[a-z]+(?=\sbag)')  # matches '[word word]' when preceded by '[number][space]' and followed by ' bag'


#print(len(fillerbags))

def bagcheck(bagindex):
        global bagcounter
        global lister
        line = testfile[bagindex]
        print('>Bag to check: ' + 'L' + str(bagindex) + ' G' + str(lister) + ' - ' + line)

        fillerbags = prog.findall(line)
        if len(fillerbags)==0:
                print('>>>Contains no bags')
                pass
        if len(fillerbags)>0:
                for y in range(len(fillerbags)):
                        if fillerbags[y] == 'shiny gold':
                                bagcounter += 1
                                print('Gotcha: ' + line)
                                print('Bag counter: ' + str(bagcounter))
                                bagindex = lister
                                break


                        else:
                                for i in testfile:
                                        if i.startswith(fillerbags[y]):
                                                newindex = testfile.index(i)
                                                bagcheck(newindex)

for q in range(len(testfile)):
        lister = q
        bagcheck(q)

print(str(bagcounter))