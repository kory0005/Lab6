import csv


fileName = input('Enter a file name: ')

fin = open(fileName, "r")
lc = 1
moveOn = 1
while (moveOn == 1):
    for line in fin:
        c = line[-1]
        # print(line)
        print(list(line))
        moveOn = 0
    lc = lc + 1

fin.close()

readTextFile(fileName)