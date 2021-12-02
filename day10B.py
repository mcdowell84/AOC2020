file = open('input/input10.txt', 'r')
input = file.readlines()
input = [x.replace('\n', '') for x in input]

for i in range(len(input)):
        input[i] = int(input[i])

testinput =     [28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3]

input = testinput

input.sort()

init = 0
jolt1 = 0
jolt3 = 0

for i in range(len(input)):
        if input[i] - init == 1:
                jolt1 += 1
        if input[i] - init == 3:
                jolt3 += 1
        init = input[i]

jolt3 += 1
print(str(jolt1*jolt3))