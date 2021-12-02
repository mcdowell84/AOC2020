# oplossing gejat van reddit

file = open('input/input09b.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

for i in range(len(input)):
        input[i] = int(input[i])

def valid(target, previous_25):
        for a in previous_25:
                for b in previous_25:
                        if a + b == target and a != b:

                                return True
        return False

for foo in range(25, len(input)):
        target = input[foo]
        previous_25 = input[foo-25:foo]
        if valid(target, previous_25) == False:
                print('false: index= ' + str(foo) + ' item=' + str(input[foo]))