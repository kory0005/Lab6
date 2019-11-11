import csv

def readTextFile(name):
    fin = open(name, "r")
    lc = 0
    moveOn = 1
    while (moveOn == 1):
        for line in fin:
            c = line[-1]
            print(list(line))
            moveOn = 0
        lc = lc + 1

    fin.close()

# readTextFile("2000_BoysNames.txt")
readTextFile("2000_GirlsNames.txt")