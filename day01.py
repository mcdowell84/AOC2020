input01 = open('input01.txt', 'r')
#print(list.read())
myList = input01.readlines()
list2 = [x.replace('\n', '') for x in myList]

#list2 = [1,3,5,11]
for i in range(len(list2)):
    for x in range(len(list2)):
        if int(list2[i]) + int(list2[x]) == 2020:
            print('succes!')
            print(list2[i])
            print(list2[x])
            c = int(list2[i]) * int(list2[x])
            print(c)
