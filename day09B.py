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



goal = 466456641

def conrange(start):
        global goal
        sum = 0
        a = start
        while sum < goal:
                sum = sum + input[a]
                a = a + 1
        if sum == goal:

                return a
        if sum > goal:
                return False

for i in range(len(input)):
        a = conrange(i)
        if a != False:
                newlist = input[i:a]

                newlist.sort()




answer = 37205496 + 18527440
print(str(answer))