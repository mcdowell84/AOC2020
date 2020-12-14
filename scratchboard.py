file = open('input/input09.txt', 'r')
myFile = file.readlines()
myFile = [x.replace('\n', '') for x in myFile]
input = myFile

lijst2 = input[0:5]
print(lijst2)