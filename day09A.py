input = [35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576]

file = open('input/input09.txt', 'r')
myFile = file.readlines()
myFile = [x.replace('\n', '') for x in myFile]
input = myFile

correct = []


def checker(x):
        line = int(input[x]) # number to be checked
        test = 'unsolved'
        begin = x-25
        end = x-1

        if begin >= 0:

                for i in range(begin, end):

                        check1 = int(input[i]) # first digit of sum

                        for o in range(begin, end): # second digit of sum
                                check2 = int(input[o])

                                if o != i and check2+check1 == line:
                                        return True


                        return False


for foo in range(25, len(input)):
        unsolved = checker(foo)
        if unsolved == False:
                correct.append(foo)

answer = correct[0]
print(answer)
